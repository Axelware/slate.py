import enum


__all__ = [
    "TrackEndReason",
    "ExceptionSeverity",
]


class TrackEndReason(enum.Enum):
    FINISHED = "FINISHED"
    LOAD_FAILED = "LOAD_FAILED"
    STOPPED = "STOPPED"
    REPLACED = "REPLACED"
    CLEANUP = "CLEANUP"


class ExceptionSeverity(enum.Enum):
    COMMON = "COMMON"
    SUSPICIOUS = "SUSPICIOUS"
    FATAL = "FATAL"
