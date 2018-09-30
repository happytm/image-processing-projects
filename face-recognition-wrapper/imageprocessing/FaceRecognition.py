import ntpath
from typing import List

import face_recognition

from model.DetectedFace import DetectedFace


class FaceRecognition:
    def __init__(self):
        self.__known_face_encodings = []
        self.__known_face_filenames = []

    def find(self, image) -> List[DetectedFace]:
        rgb_frame = image[:, :, ::-1]
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        if face_locations == []:
            return []
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        faces = []
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # for each face found try to match against known faces
            matches = face_recognition.compare_faces(self.__known_face_encodings, face_encoding)
            filename = None
            if True in matches:
                # the face matches known faces in memory so we update filename with the known filename
                first_match_index = matches.index(True)
                filename = self.__known_face_filenames[first_match_index]

            faces.append(DetectedFace(filename, top, right, bottom, left))

        return faces

    def load_face(self, filepath: str):
        image = face_recognition.load_image_file(filepath)
        self.__known_face_encodings.append(face_recognition.face_encodings(image)[0])
        self.__known_face_filenames.append(self.__get_filename_without_extension(filepath))

    def load_faces(self, filepaths: List[str]):
        [self.load_face(file) for file in filepaths]

    def delete_face(self, filepath: str):
        self.__known_face_filenames.remove(self.__get_filename_without_extension(filepath))

    def __get_filename_without_extension(self, filepath: str) -> str:
        return ntpath.basename(filepath).split('.')[0]