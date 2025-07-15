from pydantic import BaseModel


class OrderCompletedResponse(BaseModel):
    completed_order_count : int
