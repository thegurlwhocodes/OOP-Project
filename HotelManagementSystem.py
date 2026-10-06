class Guest:
  def __init__(self,name, age, phone, email):
    self.name = name
    self.age = age
    self.phone = phone
    self.email= email
  def show_guest_info(self):
    print("\n  Guest Information")
    print("Name :",self.name)
    print("Age :",self.age)
    print("Phone :",self.phone)
    print("Email :",self.email)

class Room:
  def __init__(self,room_num,room_type,price_per_night):
    self.room_num = room_num
    self.room_type = room_type
    self.price_per_night = price_per_night
    self.is_available = True
    
  def _show_room_info(self):
    print("\n   Room Information")
    print("Room Number     :", self.room_num)
    print("Room Type       :", self.room_type)
    print("Price per night :", self.price_per_night)
    print("Available       :", self.is_available)

class Reservation:
  def __init__(self,guest,room,nights):
    self.guest = guest
    self.room = room
    self.nights = nights
    self.total_price = room.price_per_night*nights
  def book_room(self):
    if self.room.is_available:
      self.room.is_available = False
      print("\n Room Booked Successfully!")
      self.guest.show_guest_info()
            print("\n RESERVATION INFORMATION ")
            print("Room Number       :", self.room.room_number)
            print("Room Type         :", self.room.room_type)
            print("Number of Nights  :", self.nights)
            print("Total Bill        :", self.total_price)
        else:
            print("\nSorry! This room is already booked.")

class security:
  def __init__(self):
    self.your_name = {}
  def add_guest(self, name, guest, reservation):
        self.your_name[name] = {"guest": guest,"reservation": reservation}
  def login(self):
        print(" Welcome to the ROYAL PALACE HOTEL!")
        name = input("\nEnter your Full Name  : ")
        if name in self.your_name:
            print("\nAccess Granted!")
            data = self.your_name[name]
            guest = data["guest"]
            reservation = data["reservation"]
            guest.show_guest_info()

            print("\n    ROOM INFORMATION   ")
            print("Room Number     :", reservation.room.room_number)
            print("Room Type       :", reservation.room.room_type)
            print("Price per Night :", reservation.room.price_per_night)
            print("Nights          :", reservation.nights)
            print("Total Bill      : Rs.", reservation.total_price)
        else:
            print("\nEnter valid name!")
            print("Access Denied.")

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_available_rooms(self):
        print("\n AVAILABLE ROOMS ")

        for room in self.rooms:
            if room.is_available:
                print("Room:", room.room_number,"Type:", room.room_type,"Price:", room.price_per_night)    

# HOTEL
hotel = Hotel("Royal Palace Hotel")
# ROOMS
room1 = Room(101, "Single Room", 5000)
room2 = Room(102, "Double Room", 8000)
room3 = Room(103, "Suite", 12000)
room4 = Room(104, "Single Room", 5000)
room5 = Room(105, "Double Room", 8000)

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)
hotel.add_room(room4)
hotel.add_room(room5)

# GUESTS
guest1 = Guest("Muntaha Imran",22,"03123456789","muntaha1234@gmail.com")
guest2 = Guest("Ayesha Khan",24,"03211111111","ayesha@gmail.com")
guest3 = Guest("Ali Ahmed",25,"03322222222","ali@gmail.com")
guest4 = Guest("Sara Malik",21,"03433333333","sara@gmail.com")
guest5 = Guest("Hamza Sheikh",27,"03544444444","hamza@gmail.com")

# RESERVATIONS
reservation1 = Reservation(guest1, room1, 4)
reservation2 = Reservation(guest2, room2, 3)
reservation3 = Reservation(guest3, room3, 2)
reservation4 = Reservation(guest4, room4, 5)
reservation5 = Reservation(guest5, room5, 1)

# BOOK ROOMS
# reservation1.book_room()
# reservation2.book_room()
# reservation3.book_room()
# reservation4.book_room()
# reservation5.book_room()

# SECURITY
security = Security()
security.add_guest("Muntaha Imran", guest1, reservation1)
security.add_guest("Ayesha Khan", guest2, reservation2)
security.add_guest("Ali Ahmed", guest3, reservation3)
security.add_guest("Sara Malik", guest4, reservation4)
security.add_guest("Hamza Sheikh", guest5, reservation5)

# LOGIN
# hotel.Hotel()
security.login()

# guest no 1 ka naam  Muntaha Imran
# guest no 2 ka naam Ayesha Khan
# guest no 3 ka naam Ali Ahmed
# guest no 4 ka naam Sara Malik
# guest no 5 ka naam Hamza Sheikh
