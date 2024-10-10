from pyannote.audio import Model
from pyannote.audio.pipelines import VoiceActivityDetection

if __name__ == "__main__":
    model = Model.from_pretrained(
        "pyannote/segmentation-3.0",
        use_auth_token="<your-token>"
    )
    pipeline = VoiceActivityDetection(segmentation=model)

    HYPER_PARAMETERS = {
        # remove speech regions shorter than that many seconds.
        "min_duration_on": 0.0,
        # fill non-speech regions shorter than that many seconds.
        "min_duration_off": 0.0
    }
    pipeline.instantiate(HYPER_PARAMETERS)
    vad = pipeline(r"..\..\data\examples\audio.mp3")
    print("test")
