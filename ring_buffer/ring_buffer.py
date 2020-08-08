class RingBuffer:

    def __init__(self, capacity):
        self.capacity = capacity # TOTAL NUMBER OF VALUES THAT CAN BE STORED IN BUFFER
        self.current_index = 0 # START THE INDEX AT ZERO
        self.stored_values = [None]*capacity # IMMUTABLE OBJECT 'None" MULTIPLIED BY VALUE 'capacity', TO REPRESENT NUMBER OF STORED VALUES (IN WAY THAT STILL SUPPORTS ITEM ASSIGNMENT)

    def append(self, item): # FUNCTION: ADDS THE GIVEN ELEMENT TO THE BUFFER
        self.stored_values[self.current_index] = item
        self.current_index += 1
        if self.current_index == self.capacity:
            self.current_index = 0

    def get(self): # FUNCTION: RETURNS ALL OF THE ELEMENTS IN THE BUFFER IN A LIST IN THEIR GIVEN ORDER; SHOULD NOT RETURN ANY 'None` VALUES, EVEN IF THEY ARE PRESENT IN THE RING BUFFER.
        # ACCOUNT FOR EMTPY RING BUFFER
        if self == None:
            return self.stored_values # THIS WAY NO 'None' VALUE IS RETURNED, IF EMPTY
        # RETURN VALUES WITH 'None` VALUES REMOVED, IF ANY ARE PRESENT IN RING BUFFER
        else:
            return [value for value in self.stored_values if value is not None]