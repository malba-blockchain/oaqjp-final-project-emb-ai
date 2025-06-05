"""Flask app for emotion detection"""
from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """Emotion detection endpoint"""
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Handle empty text
    if not text_to_analyze.strip():
        return jsonify({'error': 'Invalid text! Please try again!'})

    try:
        # Call the emotion detection function
        result = emotion_detector(text_to_analyze)

        # Format the response message
        if result['dominant_emotion'] is None:
            response_message = "Invalid text! Please try again!"
        else:
            response_message = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, "
                f"'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )

        return response_message

    except Exception as e:  # pylint: disable=broad-exception-caught
        return jsonify({'error': f'Error processing request: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
