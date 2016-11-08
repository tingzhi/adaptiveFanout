'''
 *
 * Copyright (c) 2015 Tingzhi Li, and Marco Falke
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Tingzhi Li <vincentltz at gmail dot com>
 *	   Marco Falke
 *
'''

import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import statsUtility
import glob
import errno

class result:
	def __init__ (self):
		self.expectation = 0
		self.median = 0
		self.stdev = 0
		self.var = 0
		self.mini = 0
		self.maxi = 0
		self.data = []

	def printResult(self, units):
		print "Average = {:.3f}{:s}".format(self.expectation,units)
		print "Median = {:.3f}{:s}".format(self.median,units)
		print "Standard Dev = {:.3f}{:s}".format(self.stdev,units)
		print "Variance = {:.3f}".format(self.var)
		print "Minimum = {:.3f}{:s}".format(self.mini,units)
		print "Maximum = {:.3f}{:s}".format(self.maxi,units)

	def printResultNoText(self):
		print "{:.3f},{:.3f}".format(self.expectation, self.stdev)

	def plotHistogram(self, numBin, xlab):
		fig, ax = plt.subplots()
		n, bins, patches = plt.hist(self.data, numBin, normed=0, facecolor='green', alpha=0.5)

		# get the corners of the histogram
		left = np.array(bins[:-1])
		right = np.array(bins[1:])
		bottom = np.zeros(len(left))
		top = bottom + n

		ax.set_xlim(left[0], right[-1])
		ax.set_ylim(bottom.min(), top.max()*1.2)

		plt.plot(bins)
		plt.xlabel(xlab)
		plt.ylabel('Frequency')
		plt.title('Distribution of ' + xlab)

		# Tweak spacing to prevent clipping of ylabel
		plt.subplots_adjust(left=0.15)
		plt.show()

def printCombinedResults(timeResults, hopResults, avgMsgResults):
	print "{:.3f}".format(timeResults.expectation),
	print ",",
	print "{:.3f}".format(timeResults.median),
	print ",",
	print "{:.3f}".format(timeResults.stdev),
	print ",",
	print "{:.3f}".format(timeResults.mini),
	print ",",
	print "{:.3f}".format(timeResults.maxi),
	print ",",
	print "{:.3f}".format(hopResults.expectation),
	print ",",
	print "{:.3f}".format(hopResults.median),
	print ",",
	print "{:.3f}".format(hopResults.stdev),
	print ",",
	print "{:.3f}".format(hopResults.mini),
	print ",",
	print "{:.3f}".format(hopResults.maxi),
	print ",",
	print "{:.3f}".format(avgMsgResults.expectation),
	print ",",
	print "{:.3f}".format(avgMsgResults.median),
	print ",",
	print "{:.3f}".format(avgMsgResults.stdev),
	print ",",
	print "{:.3f}".format(avgMsgResults.mini),
	print ",",
	print "{:.3f}".format(avgMsgResults.maxi)

#	print timeResults.printResultNoText()

def runStats(ls):
	ret = result()
	ret.mini = min(ls)
	ret.maxi = max(ls)
	ret.expectation = np.mean(ls)
	ret.var = np.var(ls)
	ret.median = np.median(ls)
	ret.stdev = np.std(ls)
	ret.data = ls
	return ret

def main():

	# files = []
	# for i in range(10, 210, 10):
	# 	path = 'data/overhead/overhead_' + str(i) + '.txt'
	# 	#print path
	# 	files.append(path)

	path = []
	for i in range(10, 100, 40):
		temp = 'noIdleCurrentData/fanout10/brTime_' + str(i) + '/brTime_' + str(i) + '_*.txt'
		path.append(temp)

	temp = 'noIdleCurrentData/fanout10/brTime_150/brTime_150_*.txt'
	path.append(temp)

	print 'path variable is ' + str(path)

	avgList = []
	numList = []  # avg number of broadcasting messages
	for j in range(len(path)):
		files=glob.glob(path[j])  # one case e.g 10 nodes 85 files
		print len(files)

		brTime = []
		for filename in files:
			new = []
			try:
				templs = statsUtility.ReadFileLines(filename)
			except IOError as exc:
				if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
					raise # Propagate other kinds of IOError.

			for el in templs:
				new.append(float(el))
			brTime.append(new)

		# print 'here!!!\n'
		# for i in range(len(brTime)):
		# 	print len(brTime[i])
		# print 'end here!!!\n'

		sum = 0.0
		for el in brTime:
			sum = sum + len(el)

		temp = sum / len(brTime)
		numList.append(temp)


		expList = []
		for i in range(len(brTime)):
		# ls = []
		# for j in range(len(spreadTime)):
		# 	ls.append(spreadTime[j][i])
			expectation = np.mean(brTime[i])
			# print expectation
			expList.append(expectation)

		avg = np.mean(expList)
		avgList.append(avg)
		print 'Broadcast time: ' + str(avg)

	# print avgList

	for el in avgList:
		statsUtility.AppendToFile("noIdle_avgBrTime_10.txt", str(el)+'\n')

	#print numList
	for el in numList:
		statsUtility.AppendToFile("noIdle_avgBrNum_10.txt", str(el)+'\n')

	# print len(expList)
	# for el in expList:
	# 	statsUtility.AppendToFile("testBrTime_10.txt", str(el)+'\n')



	#print minSize
	#print ls

	#print (spreadTime[84][112] == None)
	#np.mean(ls)
	#new = []
	#for i in len(spreadTime):
	#	for j in len()
	#	new.append(spreadTime[i][j])



	#timeResult = runStats(spreadtime)
	#hopResult = runStats(spreadhops)
    #	avgMsgResults = runStats(avgMsg)

#	print "Max Time Analysis Result"
#	timeResult.printResult("s")
#	print ""

#	print "Max Hops Analysis Result"
#	hopResult.printResult("")
	#printCombinedResults(timeResult, hopResult, avgMsgResults)
#	timeResult.plotHistogram(int(timeResult.maxi/2)+1, "Max Time")
#	hopResult.plotHistogram(hopResult.maxi+1, "Max Hops")

if __name__ == '__main__':
	main()
