# synthcity absolute
from synthcity.utils.datasets.time_series.sine import SineDataloader


def test_dataloader() -> None:
    loader = SineDataloader(
        no=5, seq_len=10, temporal_dim=15, static_dim=3, freq_scale=0.5
    )

    static_data, temporal_data, outcome = loader.load()

    assert static_data.shape == (5, 3)
    assert outcome.shape == (5, 1)
    assert len(temporal_data) == 5
    for item in temporal_data:
        assert item.shape == (10, 15)