from abc import ABC, abstractmethod


class ITimingManager(ABC):
    @abstractmethod
    def get_timing_summary(self) -> dict:
        raise NotImplementedError()


class IDataAggregatorTask(ABC):
    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError()
