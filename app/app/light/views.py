from fastapi import APIRouter, HTTPException

from app.utils.serial_utils import serial_communicator


router = APIRouter(
    prefix="/light",
    tags = ['light'],
)

@router.get('/{command}')
async def execute(command: str) -> None:
    if command == "on":
        serial_communicator.write_to_port('e')
    elif command == "off":
        serial_communicator.write_to_port('d')
    # elif command == "blink":
    #     serial.write_to_port('b')
    else:
        return HTTPException(status_code=400, detail="Unknown command")

    return