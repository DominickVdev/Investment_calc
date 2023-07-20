"""
Program: investmentGUI.py
Author: Dominick Vera 07/14/2023

GUI - based version of the ivestment calculator app from chapter 3. Also illustrates the use f the Text Area component.

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly.

"""

from breezypythongui import EasyFrame
#Other imports go here

#Class header
class TextAreaDemo(EasyFrame):
	# Definition of our class contructor method 
	def __init__(self):
		EasyFrame.__init__(self, title = "Investment Calculator", background = "darkslateblue")

		#Create and add the components to the window 
		self.addLabel(text = "Initial investment amount", row = 0, column = 0)
		self.addLabel(text = "Number of years", row = 1, column = 0)
		self.addLabel(text = "Interest rate in %", row = 2, column = 0)

		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addFloatField(value = 0.0, row = 2, column = 1)

		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.outputArea["background"] = "black"
		self.outputArea["foreground"] = "white"

		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.compute["background"] = "goldenrod"
		self.compute["foreground"] = "white"

	# Definition of the compute() function 
	def compute(self):
		""" Computes the investment schedule based on the inputs and outputs the scedule. """
		# Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber() / 100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years ==0:
			return

		# Set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting balance", "Interest", "Ending balance")

		# Compute and append the results for each year
		totalInterest = 0.0

		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		#Append the totals for the period 
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		#Output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"


	
# Definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	TextAreaDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()