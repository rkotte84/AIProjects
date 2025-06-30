import os
import azure.cognitiveservices.speech as speechsdk

# Get Azure Speech service endpoint and key from environment variables
service_region = os.getenv("AZURE_SPEECH_SERVICE")  # e.g., "eastus"
key = os.getenv("AZURE_SPEECH_KEY")

def speech_to_text(audio_file_path: str):
    """
    Converts speech in an audio file to text using Azure Speech service.
    """
    speech_config = speechsdk.SpeechConfig(subscription=key, region=service_region)
    audio_config = speechsdk.AudioConfig(filename=audio_file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print(f"Transcribing {audio_file_path}...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized:", result.text)
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")
    return None

if __name__ == "__main__":
    # Example usage: replace 'your_audio.wav' with your audio file path
    speech_to_text("your_audio.wav")


