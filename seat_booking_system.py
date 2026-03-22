import pandas as pd

#-----------------Functions-----------------------


"""
This function checks whether at least one seat is fully available
from source to destination
"""
def check_availability(source, destination, seat_data, stops):
    found = False

    start = stops.index(source)
    end = stops.index(destination)

    for seat in range(len(seat_data)):
        is_available = True

        for stop in range(start, end):
            if seat_data.loc[seat, stops[stop]] == 1:
                is_available = False
                break

        if is_available:
            print(f"Seat {seat} is Available")
            found = True

    return found


"""
This function books a seat from source to destination.
If any segment is already booked, it rolls back previous changes.
"""
def book_seat(source, destination, seat_data, stops, seat_no):
    start = stops.index(source)
    end = stops.index(destination)

    for i in range(start, end):
        if seat_data.loc[seat_no, stops[i]] == 0:
            seat_data.loc[seat_no, stops[i]] = 1
        else:
            # rollback
            for j in range(start, i):
                seat_data.loc[seat_no, stops[j]] = 0

            print("Selected seat not available")
            #return False

    print("Seat booked successfully")
    #return True


"""
This function displays continuous free segments for each seat
between source and destination.(in btw Range)
"""
def show_segmented_seats(source, destination, seat_data, stops):
    start = stops.index(source)
    end = stops.index(destination)

    for seat in range(len(seat_data)):
        segment = []

        for i in range(start, end):
            if seat_data.loc[seat, stops[i]] == 0:
                segment.append(stops[i])
            else:
                if segment:
                    print(f"Seat {seat}: {segment[0]} → {stops[i]}")
                    segment = []
        if segment:
            print(f"Seat {seat}: {segment[0]} → {stops[end]}")


"""
This function displays continuous free segments for each seat
between source and destination.
"""
def path_exists(source, destination, seat_data, stops):
    start = stops.index(source)
    end = stops.index(destination)

    for i in range(start, end):
        segment_available = False

        for seat in range(len(seat_data)):
            if seat_data.iloc[seat, i] == 0:
                segment_available = True
                break

        if not segment_available:
            return False

    return True
    

"""
 This function allows booking seats in segments (step-by-step).
 User selects intermediate stops and seats manually.
"""
def book_segement_seats(source, destination, seat_data, stops):
    temp_source = source
    while (temp_source!=destination):
        temp_destination = input(f"Eneter the destination from {temp_source} : ").upper()
        seat_no = int(input("Eneter the seat number : "))
        book_seat(temp_source, temp_destination, seat_data, stops, seat_no)
        temp_source = temp_destination




#Code 
seat_data = pd.read_csv("/home/rgukt/Documents/python/seg.csv")
stops = list(seat_data.columns)[1:]
source = input("Enter the boarding point : ").upper()
destination = input("Enter the droping point : ").upper()

if(check_availability(source, destination, seat_data, stops)):
    seat_no = int(input("Enter the seatNo : "))
    book_seat(source, destination, seat_data, stops, seat_no)
else :
    print("Seats not-availale")
    segment_permission = input("Do you want to go with segemented seats (Yes/No): ").upper()
    if(segment_permission=="YES"):
        if(path_exists(source, destination, seat_data, stops)):
            show_segmented_seats(source, destination, seat_data, stops)
            book_segement_seats(source, destination, seat_data, stops)
        else:
            print("Segemented seats not available")
    else :
        pass
