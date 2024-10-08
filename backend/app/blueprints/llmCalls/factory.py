from .metrics import Metrics
from .percentages import Percentages
from .summary import Summary
from .bulkSummaries import Bulk
from enum import Enum


class LLMCallFactory:
    class RequestType(Enum):
        SUMMARY = "SUMMARY"
        PERCENTAGES = "PERCENTAGES"
        METRICS = "METRICS"
        BULK = "BULK"

    # takes in the request type, returns the handler class object, instantiated
    def getHandler(requestType: str, data: dict):
        if requestType == LLMCallFactory.RequestType.METRICS:
            object = Metrics(data)
        elif requestType == LLMCallFactory.RequestType.PERCENTAGES:
            object = Percentages(data)
        elif requestType == LLMCallFactory.RequestType.SUMMARY:
            object = Summary(data)
        elif requestType == LLMCallFactory.RequestType.BULK:
            object = Bulk(data)
        else:
            # if the request type doesn't exist throw an error
            raise ValueError("not a valid request")

        return object.handleRequest()
