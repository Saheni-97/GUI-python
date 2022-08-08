from tkinter import *
from math import *
from PIL import *

from tkinter import ttk
import PIL
import math
import ctypes    

window = Tk()
window.title('MEP GUI')

roomarea = StringVar(window)
ledopencheck = StringVar(window)
ledpopup = StringVar(window)
devicedriverpopup = StringVar(window)
mcbpopup = StringVar(window)
ledpopup.set(0);
devicedriverpopup.set(0);
mcbpopup.set(0);

window.geometry("740x480")
window.maxsize(740, 480)
window.minsize(740, 480)
my_canvas = Canvas(window, width=780, height=500)
frame1=Frame(window, width=120,highlightbackground='grey',highlightthickness=1,relief=RIDGE)
frame1.grid(padx=50,pady=30,ipadx=215,ipady=200)

pic=Canvas(window,width=780,height=500)
img = PhotoImage(file="p6.png")
pic.create_image(70,20, image=img)


Label(window, text="Building Services:").place(x=60, y=40)


def on_click(event):
	choice = event.widget.get()
	if choice == "Electrical":
		
		L1.place(x=65, y=80)
	  
		# drop2.place(x=200,y=196)
		# drop2.config(height=1,width=18)
		L2.place(x=65, y=120)
		# drop3.place(x=200,y=246)
		# drop3.config(height=1,width=18)
		L3.place(x=310, y=120)
##		drop8.place(x=400, y=115)
##		drop8.config(height=1, width=18,bg='lightsteelblue1')		
		cmb2.place(x=400, y=120)	
		L4.place(x=65, y=160)
##		drop4.place(x=150, y=155)
##		drop4.config(height=1, width=18,bg='lightsteelblue1')
		cmb3.place(x=160, y=160)
		L5.place(x=65, y=250)
##		drop5.place(x=150, y=245)
##		drop5.config(height=1, width=18,bg='lightsteelblue1')
		cmb4.place(x=160, y=250)
		L6.place_forget()
		L7.place_forget()
		L8.place_forget()
		L9.place_forget()
		L10.place_forget()
		cmb5.place_forget()
		cmb6.place_forget()

	if choice == "HVAC":
		
		L6.place(x=60, y=100)
		# drop2.place(x=200,y=196)
		# drop2.config(height=1,width=18)
		L7.place(x=60, y=140)
		# drop3.place(x=200,y=246)
		# drop3.config(height=1,width=18)
		L8.place(x=800, y=250)
		# drop6.place(x=1000,y=246)
		# drop6.config(height=1,width=18)
		L9.place(x=60, y=180)
		cmb5.place(x=160, y=180)
		#drop6.config(height=1, width=18,bg='lightsteelblue1')
		L10.place(x=60, y=270)
		cmb6.place(x=160, y=270)
		#drop7.config(height=1, width=18,bg='lightsteelblue1')
		L1.place_forget()
		L2.place_forget()
		L3.place_forget()
		L4.place_forget()
		L5.place_forget()
		cmb2.place_forget()
		cmb3.place_forget()
		cmb4.place_forget()


##	if choice == "Plumbing":
##                L1.place_forget()
##                L2.place_forget()
##                L3.place_forget()
##                L4.place_forget()
##                L5.place_forget()
##                L6.place_forget()
##                L7.place_forget()
##                L8.place_forget()
##                L9.place_forget()
##                L10.place_forget()
##                cmb2.place_forget()
##                cmb3.place_forget()
##                cmb4.place_forget()
##                cmb5.place_forget()
##                cmb6.place_forget()


num = ["Electrical", "HVAC", "Plumbing", "Fire"]
cmb=ttk.Combobox(window,value=num,width=17)
cmb.place(x=160, y=40)
cmb.bind("<<ComboboxSelected>>", on_click)
#cmb.grid(row=0,column=0)
L1 = Label(window, text="Electrical:")
#Ll.pack(padx=5,pady=5)
L2 = Label(window, text="Load:")
L3 = Label(window, text="Component:")
L4 = Label(window, text="24V DC:")
L5 = Label(window, text="230V AC:")
# Hvac
L6 = Label(window, text="Load Calculation:")
L7 = Label(window, text="Heat Load:")
L8 = Label(window, text="Ventilation Load:")
L9 = Label(window, text="System:")
L10 =Label(window, text="Component:")

variable = StringVar(window)
variable.set("Select")

#drop1 = OptionMenu(window, variable, *num, command=on_click)



#drop1.place(x=160, y=35)
#drop1.config(height=1, width=18,bg='lightsteelblue1')

##num1 = ["Load Calculation", "Component Selection"]
##
##variable1 = StringVar(window)
##variable1.set("Select")
##
##drop2 = OptionMenu(window, variable1, *num1)
##
##num2 = ["24V DC", "230V AC"]
##
##variable2 = StringVar(window)
##variable2.set("Select")
##
##drop3 = OptionMenu(window, variable2, *num2)




def open_popup(event):
	choice = event.widget.get()
	if ledpopup.get() == '0':		
		if choice == 'LEDs':
			top = Toplevel(window)
			
			top.geometry("480x450")
			top.maxsize(480,450)
			top.minsize(480,450)
			top.title("LEDs")
			
			Label(top, text="Lighting Calculation").place(x=200, y=30)
			f2=Frame(top, width=50,highlightbackground='grey',highlightthickness=1)
			f2.grid(padx=50,pady=60,ipadx=180,ipady=70)
			# Label(top, text= "Number of rooms").place(x=150,y=90)
			# e1=Entry(top).place(x=400,y=100)
			Label(top, text="Room Type").place(x=90, y=90)
			num8 = ['Bed Room','Study Room','Living Room','Dining Room','Kitchen','Wash Room']
			cmb1=ttk.Combobox(top,value=num8,width=17)
			cmb1.place(x=200, y=90)
			cmb1.bind("<<ComboboxSelected>>", open_popup)
	
			Label(top, text="Room Area",height=0, width=10).place(x=85, y=130)
			e3 = Entry(top)
			e3.configure(justify='center')
			e3.place(x=200, y=130)
			Label(top, text="sqm").place(x=350, y=130)
			Label(top, text="Lux").place(x=90, y=160)
			e4 = Entry(top)
			e4.configure(justify='center')
			e4.place(x=200, y=160)
			Label(top, text="Lumens/Sqm").place(x=350, y=160)
			frame3=Frame(top, width=50,highlightbackground='grey',highlightthickness=1)
			#device_drivers.place_forget()
			ledopencheck.set(1);
			ledpopup.set(1);

			
			def calculate(widget):
				#list=['200','300','150','150','300','150']
				#for i in range(len(cost)):
				lumens = float(float(e3.get()) * float(e4.get()))
				roomarea.set(float(e3.get()));
				watt = lumens / 100
				leds = ceil(watt / 10.08)
				zones = ceil(leds / 5)
				dd = ceil(zones / 5)		
				l1 = Label(top, text="Result:" )
				l2 = Label(top, text="No. of LEDs")
				e5 = Text(top, height=1, width=15)
				
				
				l3 = Label(top, text="No. of Zones")			
				e6 = Text(top, height=1, width=15)
				
				l4 = Label(top, text="No. of Device Drivers")			
				e7 = Text(top, height=1, width=15)
				

				
				widget.grid_forget()
				

				widget.grid(padx=50,pady=10,ipadx=180,ipady=50)
				l1.place(x=20, y=250)
				l2.place(x=80, y=280)
				e5.place(x=200, y=280)
				
				e5.delete("1.0","end")
				e5.tag_configure("math.ceil(leds)" , justify='center' )
				e5.insert(END, leds)
				e5.config(state="disabled")
				e5.tag_add("math.ceil(leds)","1.0","end")



				e6.delete("1.0","end")
				e6.tag_configure("math.ceil(zones)" ,justify='center')
				e6.insert(END, math.ceil(zones))
				e6.config(state="disabled")
				e6.tag_add("math.ceil(zones)","1.0","end")


				e7.delete("1.0","end")
				e7.tag_configure("math.ceil(dd)" ,justify='center')
				e7.insert(INSERT, dd)
				e7.config(state="disabled")
				e7.tag_add("math.ceil(dd)","1.0","end")


				

				
				l3.place(x=80, y=310)
				e6.place(x=200, y=310)
				
				
				l4.place(x=80, y=340)
				e7.place(x=200, y=340)
				
						
				
			def closeLed():
				ledpopup.set(0);
				top.destroy()


			Button(top, text="Calculate", bg="lightsteelblue1", height=1, width=16, command= lambda : calculate(frame3)).place(x=200, y=220)
			Button(top, text="Exit", bg="lightsteelblue1", height=1, width=12, command=closeLed).place(x=215, y=380)
	

	if ledopencheck.get() == '1':
		if devicedriverpopup.get() == '0':
			if choice == 'Device Drivers':
				top = Toplevel(window)
				
				top.geometry("500x400")
				top.maxsize(500,400)
				top.minsize(500,400)
				top.title("Device Drivers")
							
				Label(top, text="Device Drivers").place(x=200, y=30)
				# Label(top, text= "Number of rooms").place(x=150,y=90)
				# e1=Entry(top).place(x=400,y=100)
				Label(top, text="Total Lux").place(x=100, y=90)
				e8 = Entry(top)
				e8.configure(justify='center')
				e8.place(x=300, y=90)
				frame4=Frame(top, width=50,highlightbackground='grey',highlightthickness=1)
				frame4.grid(padx=50,pady=170,ipadx=190,ipady=70)
				Label(top, text="Total watt").place(x=100, y=180)
				e9 = Text(top, height=1, width=15)
				
				e9.place(x=300, y=180)
				# Label(top, text= "Sqm").place(x=550,y=120)
				Label(top, text="No. of DC LEDs").place(x=100, y=210)
				e10 = Text(top, height=1, width=15)
				
				e10.place(x=300, y=210)
				Label(top, text="No. of Zones").place(x=100, y=240)
				e11 = Text(top, height=1, width=15)
				
				e11.place(x=300, y=240)
				Label(top, text="No. of Device Drivers").place(x=100, y=270)
				e12 = Text(top, height=1, width=15)
				
				e12.place(x=300, y=270)
				devicedriverpopup.set(1);
				
				def calc1():
					
					watt =ceil(float(float(e8.get()) * float(float(roomarea.get())/100)))
					#e6 = Entry(top).place(x=300, y=90)
					e9.delete("1.0","end")
					e9.tag_configure("math.ceil(watt)" ,justify='center')
					e9.insert(END, watt)
					e9.config(state="disabled")
					e9.tag_add("math.ceil(watt)","1.0","end")

					
					leds=ceil(watt/10)
					e10.delete("1.0","end")
					e10.tag_configure("math.ceil(leds)" ,justify='center')
					e10.insert(END, leds)
					e10.config(state="disabled")
					e10.tag_add("math.ceil(leds)","1.0","end")

					
					zones=ceil(leds/5)
					e11.delete("1.0","end")
					e11.tag_configure("math.ceil(zones)" ,justify='center')
					e11.insert(END, zones)
					e11.config(state="disabled")
					e11.tag_add("math.ceil(zones)","1.0","end")

					
					dd=ceil(zones/5)
					e12.delete("1.0","end")
					e12.tag_configure("math.ceil(dd)" ,justify='center')
					e12.insert(INSERT, dd)
					e12.config(state="disabled")
					e12.tag_add("math.ceil(dd)","1.0","end")

				def closeDD():
					devicedriverpopup.set(0);
					top.destroy()

				b3 = Button(top, text="Calculate", bg="lightsteelblue1", height=1, width=16, command = calc1).place(x=180, y=130)
				
				b4 = Button(top, text="Exit", bg="lightsteelblue1", height=1, width=12, command=closeDD).place(x=190, y=330)
	

def open_popup1(event):
	choice = event.widget.get()
	if mcbpopup.get() == '0':
		if choice == "MCB/RCCB/RCBO":
			top = Toplevel(window)
			top.geometry("800x400")
			top.maxsize(800,400)
			top.minsize(800,400)

			pic4=Canvas(top,width=700,height=700)
			pic4.place(x=100,y=100)        
			pic4.img4 = PhotoImage(file="p4.png")                                      
			pic4.create_image(340,40, image=pic4.img4)                                  

##			pic5=Canvas(top,width=800,height=400)
##			img5 = PhotoImage(file="ss1.png")
##			pic5.create_image(70,15, image=img5)
			
			top.title("CABLE RATING/ SIZE -- AS/ NZS 3008.1.2:2017")
			l0 = Label(top, text = "SINGLE PHASE AC \n 230V AC 50 Hz").grid(row=60,column=20)
			11 == Label(top, text="Supply Voltage in V").grid(row=75,column=00)
			l2_value = StringVar()
			l2 = Entry(top, textvariable=l2_value).grid(row=75,column=10)
			l6 = Label(top, text="Appliance Wattage in W").grid(row=100,column=00)
			l7_value = StringVar()
			l7 = Entry(top, textvariable=l7_value).grid(row=100,column=10)
			l8 = Label(top, text="Power Factor").grid(row=130,column=00)
			l9_value = StringVar()
			l9 = Entry(top, textvariable=l9_value).grid(row=130,column=10)
			l10 = Label(top, text="Diversity Factor").grid(row=160,column=00)
			l11_value = StringVar()
			l11 = Entry(top, textvariable=l11_value).grid(row=160,column=10)
			l3 = Label(top, text="Design Current in A").grid(row=200,column=10)
			l4 = Label(top, text="Conductor Current in A").grid(row=200,column=20)
			l5 = Label(top, text="MCB Rating in A").grid(row=200,column=30)
			l12 = Label(top, text="Conductor Size in sqmm").grid(row=200,column=40)
			t1 = Text(top, height=3, width=20)
			t1.grid(row=220,column=10)
			t2 = Text(top, height=3, width=20)
			t2.grid(row=220,column=20)
			t3 = Text(top, height=3, width=20)
			t3.grid(row=220,column=30)
			t4 = Text(top, height=3, width=20)
			t4.grid(row=220,column=40)
			pic4.place(x=120,y=240)
			#pic5.place(x=790,y=0)
			mcbpopup.set(1);


			def from_Aritra():
				x7 = float(l2_value.get())
				x8 = float(l9_value.get())
				x9 = float((l7_value.get()))
				x10 = float((l11_value.get()))
				x5 = 225.00
				x6 = 255.00
				x11 = 4000.00
				x12 = 0.00
				x13 = 0.5
				x14 = 1.0
				x15 = 0.1

				if int(x7) >= x5 and int(x7) <= x6 and int(x9) <= x11 and float(x8) >=x13 and float(x8) <=x14 and float(x10) >=x15 and float(x10) <=x14 and int(x9) != x12:
					x1 = x7*x8
					x2 = x9/x1
					desCur = x10*x2
						
					if desCur>=0.1 and desCur<=4.0:
						mcb = 6
					elif desCur>4.0 and desCur<=6:
						mcb = 8
					elif desCur>6.0 and desCur<=8:
						mcb = 10
					elif desCur>8.0 and desCur<=11:
						mcb = 13
					elif desCur>11.0 and desCur<=14:
						mcb = 16
					elif desCur>14.0 and desCur<=18:
						mcb = 20
					elif desCur>18.0 and desCur<=23:
						mcb = 25
					else:
						mcb = "WARNING -- \n CURRENT TOO HIGH"

					conCur = desCur*2.5
					if conCur>=0.1 and conCur<=2.5:
						x3 = 1.0
					elif conCur>2.5 and conCur<=6.0:
						x3 = 1.5
					elif conCur>6.0 and conCur<=15.0:
						x3 = 2.5
					elif conCur>15.0 and conCur<=22.0:
						x3 = 4.0
					elif conCur>22.0 and conCur<=30.0:
						x3 = 6.0
					else:
						x3 = "WARNING -- \n CURRENT TOO HIGH"

				elif int(x9) == x12:
					ctypes.windll.user32.MessageBoxW(0, "WARNING -- WATTAGE VALUE MUST BE GREATER THAN ZERO", "CABLE RATING/ SIZE -- 230V 50Hz", 1)
				elif int(x9) > x11:
					ctypes.windll.user32.MessageBoxW(0, "WARNING -- WATTAGE OUTSIDE LIMIT \n \t WATT MUST BE < 4000", "CABLE RATING/ SIZE -- 230V 50Hz", 1)
				elif float(x8) < x13:
					ctypes.windll.user32.MessageBoxW(0, "WARNING -- POWER FACTOR IS TOO LOW", "CABLE RATING/ SIZE -- 230V 50Hz", 1)
				elif float(x8) > x14:
					ctypes.windll.user32.MessageBoxW(0, "WARNING -- POWER FACTOR CANNOT BE > 1.0", "CABLE RATING/ SIZE -- 230V 50Hz", 1)
				elif float(x10) < x15:
					ctypes.windll.user32.MessageBoxW(0, "WARNING -- DIVERSITY FACTOR IS TOO LOW", "CABLE RATING/ SIZE -- 230V 50Hz", 1)
				elif float(x10) > x14:
					ctypes.windll.user32.MessageBoxW(0, "DIVERSITY FACTOR CANNOT BE > 1.0", "CABLE RATING/ SIZE -- 230V 50Hz", 1)
				else:
					ctypes.windll.user32.MessageBoxW(0, "WARNING -- VOLTAGE OUTSIDE LIMIT \n \t VOLT MUST BE 225-255", "CABLE RATING/ SIZE -- 230V 50Hz", 1)


				t1.delete("1.0",END)
				t1.tag_configure("desCur", justify='center', font = '5')
				t1.insert(END, round(desCur,3))
				t1.config(state="disabled")
				t1.tag_add("desCur","1.0","end")

				t2.delete("1.0", END)
				t2.tag_configure("math.ceil(conCur)", justify='center', font = '5')
				t2.insert(END, math.ceil(conCur))
				t2.config(state="disabled")
				t2.tag_add("math.ceil(conCur)","1.0","end")

				t3.delete("1.0", END)
				t3.tag_configure("math.ceil(mcb)", justify='center', font = '5')
				t3.insert(END, math.ceil(mcb))
				t3.config(state="disabled")
				t3.tag_add("math.ceil(mcb)","1.0","end")

				t4.delete("1.0",END)
				t4.tag_configure("x3", justify='center', font = '5')
				t4.insert(END, x3)
				t4.config(state="disabled")
				t4.tag_add("x3","1.0","end")

			def closeMCB():
				mcbpopup.set(0);
				top.destroy()

			b1 = Button(top, text="Calculate",height=1, width=12, command=from_Aritra ,bg='lightsteelblue1').grid(row=220,column=00)
			b2 = Button(top, text="Exit", bg="lightsteelblue1", height=1, width=12, command=closeMCB).place(x=690, y=355)



pic.place(x=600,y=00)


num3 = ["LEDs", "Device Drivers"]
cmb3=ttk.Combobox(window,value=num3,width=17)
cmb3.bind("<<ComboboxSelected>>", open_popup)

##variable3 = StringVar(window)
##variable3.set("Select")
##
##drop4 = OptionMenu(window, variable3, *num3, command=open_popup)

num4 = ["Appliances", "Power Pack 230-24V Converter", "Relays", "Power Sockets", "Device Drivers"]

cmb4=ttk.Combobox(window,value=num4,width=17)
##variable5 = StringVar(window)
##variable5.set("Select")
##drop5 = OptionMenu(window, variable5, *num4)

num5 = ["Cooling System", "Heating System", "Fresh Air System", "Exhaust System"]
cmb5=ttk.Combobox(window,value=num5,width=17)
cmb5.bind("<<ComboboxSelected>>", open_popup)
	

##variable6 = StringVar(window)
##variable6.set("Select")
##
##drop6 = OptionMenu(window, variable6, *num5)

num6 = ["VRF System", "CHW System", "DX System", "FAN System"]
cmb6=ttk.Combobox(window,value=num6,width=17)
cmb6.bind("<<ComboboxSelected>>", open_popup)

##variable7 = StringVar(window)
##variable7.set("Select")

##drop7 = OptionMenu(window, variable7, *num6)

num7 = ["MCB/RCCB/RCBO", "Cable Length/size", "Earthing", "Conduit Size/Length", "Mains Box/Distribution Box"]
cmb2=ttk.Combobox(window,value=num7,width=17)
cmb2.bind("<<ComboboxSelected>>", open_popup1)
	

##variable8 = StringVar(window)
##variable8.set("Select")
##
##drop8 = OptionMenu(window, variable8, *num7, command= open_popup1)
##


Button(window, text="Exit", bg="lightsteelblue1", height=1, width=12, command=window.destroy).place(x=470, y=390)




window.mainloop()
