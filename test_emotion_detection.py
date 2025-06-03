import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy_emotion(self):
        """Test for joy dominant emotion"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger_emotion(self):
        """Test for anger dominant emotion"""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust_emotion(self):
        """Test for disgust dominant emotion"""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness_emotion(self):
        """Test for sadness dominant emotion"""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear_emotion(self):
        """Test for fear dominant emotion"""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_response_format(self):
        """Test that the response contains all required keys"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        expected_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in expected_keys:
            self.assertIn(key, result)
    
    def test_emotion_scores_type(self):
        """Test that emotion scores are numeric"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in emotions:
            self.assertIsInstance(result[emotion], (int, float))

if __name__ == '__main__':
    unittest.main()