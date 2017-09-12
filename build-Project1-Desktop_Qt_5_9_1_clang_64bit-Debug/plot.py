from matplotlib.pyplot import *
from numpy import *
import re
import os
from subprocess import Popen, PIPE

def les_og_plot_resultater():
	max_error_list = []
	x = range(3,13)
	for i in x:
		os.system("./Project1 %.d" % 2**(i))
		output = Popen(["ls"], stdout=PIPE).communicate()[0]
		datfiler = re.findall(".*\.dat",output,re.IGNORECASE)
		for filen in datfiler:
			#numerical answer
			x_numerical, y_numerical = read_file_and_put_in_arrays(filen)
			#analytic answer
			x_analytic = linspace(0,1,len(x_numerical)+2)[1:-1]
			y_analytic = 1-(1 - exp(-10))*x_analytic - exp(-10*x_analytic);
			#error
			max_error_list.append(max(log2(abs((y_numerical-y_analytic)/y_analytic))))
			break

	plot(x,max_error_list)
	savefig("Error.pdf",bbox_inches="tight")

	output = Popen(["ls"], stdout=PIPE).communicate()[0]
	datfiler = re.findall(".*\.dat",output,re.IGNORECASE)
	for filen in datfiler:
		#numerical answer
		x_numerical, y_numerical = read_file_and_put_in_arrays(filen)
		#analytic answer
		x_analytic = linspace(0,1,len(x_numerical)+2)[1:-1]
		y_analytic = 1-(1 - exp(-10))*x_analytic - exp(-10*x_analytic);

		plot(x_numerical,y_numerical,"k-")
		plot(x_analytic,y_analytic,"g-")
		savefig("%s.pdf" % filen[:-4],bbox_inches="tight")


def read_file_and_put_in_arrays(filen):
		infile = open(filen, "r")
		x_numerical = []
		y_numerical = []
		lines = infile.readlines()
		for line in lines:
			words = line.split()
			x_numerical.append(float(words[0]))
			y_numerical.append(float(words[1]))
		return array(x_numerical),array(y_numerical)

if __name__ == '__main__':
	les_og_plot_resultater()