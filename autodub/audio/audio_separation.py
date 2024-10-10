from speechbrain.inference.separation import SepformerSeparation as separator
import torchaudio


if __name__ == "__main__":
    model = separator.from_hparams(source="speechbrain/sepformer-wsj02mix", savedir='pretrained_models/sepformer-wsj02mix')

    # for custom file, change path
    est_sources = model.separate_file(path=r"..\..\data\examples\audio.mp3")

    torchaudio.save("source1hat.wav", est_sources[:, :, 0].detach().cpu(), 8000)
    torchaudio.save("source2hat.wav", est_sources[:, :, 1].detach().cpu(), 8000)