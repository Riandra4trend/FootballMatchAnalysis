import numpy as np

class GalleryManager:
    def __init__(self, threshold=0.5):
        self.gallery = {}  # {track_id: {"embedding": np.array, "info": {...}}}
        self.threshold = threshold

    def add(self, track_id, embedding, info):
        self.gallery[track_id] = {"embedding": embedding, "info": info}

    def match(self, embedding):
        best_id = None
        best_score = float('inf')
        for track_id, data in self.gallery.items():
            dist = np.linalg.norm(data["embedding"] - embedding)
            if dist < best_score and dist < self.threshold:
                best_score = dist
                best_id = track_id
        return best_id

    def remove(self, track_id):
        if track_id in self.gallery:
            del self.gallery[track_id]