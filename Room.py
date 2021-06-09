class Room:

    def __init__(self, _room_id, _room_name):
        self._room_id = _room_id
        self._room_name = _room_name

    def __str__(self):
        return f"{self._room_id} - {self._room_name}"

    def set_room_name(self, value):
        self._room_name = value

    def get_room_name(self):
        return self._room_name

    def set_room_id(self, value):
        self._room_id = value

    # this could help for getting the room id for the plug
    def get_room_id(self):
        return self._room_id
