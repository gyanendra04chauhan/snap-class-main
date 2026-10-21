import dlib
import face_recognition_models
import numpy as np
import streamlit as st
from sklearn.svm import SVC

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    face_recognition_model = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector, shape_predictor, face_recognition_model


def get_face_embeddings(image_np):
    image_np = np.asarray(image_np)
    if image_np.ndim != 3 or image_np.shape[2] != 3:
        raise ValueError("Expected an RGB image with shape (height, width, 3).")

    detector, shape_predictor, face_recognition_model = load_dlib_models()
    faces = detector(image_np, 1)

    embeddings = []
    for face in faces:
        shape = shape_predictor(image_np, face)
        descriptor = face_recognition_model.compute_face_descriptor(
            image_np, shape, 1
        )
        embeddings.append(np.asarray(descriptor, dtype=np.float64))

    return embeddings


@st.cache_resource
def get_trained_model():
    X = []
    y = []

    for student in get_all_students() or []:
        embedding = student.get("face_embedding")
        student_id = student.get("student_id")

        if embedding is None or student_id is None:
            continue

        vector = np.asarray(embedding, dtype=np.float64)
        if vector.shape == (128,) and np.isfinite(vector).all():
            X.append(vector)
            y.append(student_id)

    if not X:
        return None

    classifier = None
    if len(set(y)) >= 2:
        classifier = SVC(
            kernel="linear",
            probability=True,
            class_weight="balanced",
        )
        classifier.fit(X, y)

    return {"clf": classifier, "X": X, "y": y}


def train_classifier():
    get_trained_model.clear()
    return get_trained_model() is not None


def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}

    model_data = get_trained_model()
    if model_data is None:
        return detected_student, [], len(encodings)

    classifier = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["y"]
    all_students = sorted(set(y_train), key=str)

    for encoding in encodings:
        if classifier is None:
            # Only one student is enrolled.
            candidate_id = all_students[0]
        else:
            candidate_id = classifier.predict([encoding])[0]

        # Compare against every saved embedding for the predicted student.
        distances = [
            np.linalg.norm(saved_embedding - encoding)
            for saved_embedding, student_id in zip(X_train, y_train)
            if student_id == candidate_id
        ]

        if distances and min(distances) <= 0.45:
            detected_student[candidate_id] = True

    return detected_student, all_students, len(encodings)