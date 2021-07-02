'''
Carbon_factory version 1.0, 2 July 2021
author: Maria Raluca Diaconescu
This program can be used to create data structures in a way 
that shows in how many ways we can use programming languages
'''

class AdjVertex():

	def __init__(self, data):

		self.vertex = data
		self.next = None
    
class Graph():

	def __init__(self, vertices):

		self.V = vertices
		self.graph = [None] * self.V


	def add_edge(self, src, dest):

		vertex = AdjVertex(dest)
		vertex.next = self.graph[src]
		self.graph[src] = vertex

		vertex = AdjVertex(src)
		vertex.next = self.graph[dest]
		self.graph[dest] = vertex


	def add_edge_f1_1(self, src, dest):

		src.next = dest
		dest.next = src



		
		
class Node:


	def __init__(self, value, info, link_node=None):

		self.value = value

		self.info = info

		self.link_node = link_node



	def set_link_node(self, link_node):

		self.link_node = link_node


	def unlink_node(self, link_node):

		self.link_node = None


	def get_link_node(self):

		return self.link_node


	def get_value(self):

		return self.value

	def set_info(self, data):

		self.info = data

	def get_info(self):

		return self.info


	def __str__(self):

		return str(self.value)




class LinkedList():


	def __init__(self, value, info=None):

		self.head_node = Node(value, info)

		self.counter = 0

		self.counter1 = 0

		self.llist_values = []

		self.data_node = []


	def get_head_node(self):

		return self.head_node


	def push(self, new_value, info=None):

		new_node = Node(new_value, info)

		new_node.link_node = self.head_node

		self.head_node = new_node



	def remove(self, value_to_remove):

		current_node = self.head_node

		if (current_node is not None):

			if current_node.value == value_to_remove:

				self.head_node = current_node.link_node

				current_node = None

				return


		while (current_node is not None):

			if current_node.value == value_to_remove:

				break

			current_node = current_node.link_node



		if (current_node == None):

			return

		next_node = current_node.link_node

		current_node.unlink_node(current_node.link_node)

		current_node.link_node = next_node.link_node



	def print_the_linked_list(self):

		self.llist_values = []

		current_node = self.head_node

		while (current_node):

			self.llist_values.append(current_node.get_value())

			current_node = current_node.link_node


		for item in self.llist_values:

			print(item)



	def get_node_value(self, idx):

		nvl= []

		current_node = self.head_node

		while (current_node):

			self.counter +=1 

			if self.counter == idx:

				nvl.append(current_node.get_value())

			current_node = current_node.link_node

		self.counter = 0

		return nvl


	def get_node_value_1(self, idx):

		nvl= []


		current_node = self.head_node

		while (current_node):

			self.counter +=1 

			if self.counter == idx:

				nvl.append(current_node.get_value())

			current_node = current_node.link_node

		self.counter = 0

		return nvl[0]



	#the methods use the information from the instantiation of classes

	def retrieve_node_instance_info(self, idx):

		nil = []

		current = self.head_node

		self.counter = 0

		while (current):

			print(current.value)

			if self.counter == idx:

				nil.append(current.value.get_info())

			self.counter += 1

			current = current.link_node

		self.counter = 0

		return nil



	def retrieve_the_info(self):

		self.data_node = []

		current_node = self.head_node

		while (current_node):

			self.data_node.append(current_node.value)

			current_node = current_node.link_node

		return self.data_node



	def retrieve_the_info_1(self):

		var_list = []

		for item in self.retrieve_the_info():

			if type(item) != int:

				print(item.info)

				var_list.append(item.info)

			else:

				break

		return var_list


	def retrieve_the_length_of_the_linked_list(self):

		self.llist_values = []

		current_node = self.head_node

		while (current_node):

			self.llist_values.append(current_node.get_value())

			current_node = current_node.link_node

		return len(self.llist_values)




class Drop():

	def __init__(self, drop):

		self.drop = drop

		print("I am a drop")


class Spindle():

	def __init__(self, spindle):

		self.spindle = spindle

		print("I am a spindle")

class Circle():

	def __init__(self, circle):

		self.circle = circle

		print("I am a circle")


class Star(Circle, Spindle, Drop):

	def __init__(self, circle, spindle, drop):

		self.circle = circle
		self.spindle = spindle
		self.drop = drop

	def relate_to_circle(self, circle):

		return Circle(circle)

	def relate_to_spindle(self, spindle):

		return Spindle(spindle)


	def relate_to_drop(self, drop):

		return Drop(drop)
			



var_Drop = Drop("Tungsten")

var_Spindle = Spindle("Sword")

var_Circle = Circle("Home")

var_Star = Star("Home", "Sword", "Tungsten")



class CarbonNet(Star, Circle, Spindle, Drop):	

	class TinyCell(Star, Circle, Spindle, Drop):


		#the Stars created inside the Star class will be different objects and 
		#the instances of the Star subclass every time the Star class is instantiated and
		# its subclasses are called 

		#if the subclass produces subclasses, it becomes a different object

		#When the initial class and the subclasses start to produce subclasses, 
		#the initial class instances will change too
		
		#the super method can directly relate subclasses to initial classes

		class Star(Star, Circle, Spindle, Drop):

			def __init__(self, circle, spindle, drop, bond=1, tiny_cell=6):

				self.bond1 = bond
				self.bond2 = bond
				self.bond3 = bond
				self.bond4 = bond
				self.bond5 = bond
				self.tiny_cell = tiny_cell
				self.star = Star(Circle(var_Circle),Spindle(var_Spindle),Drop(var_Drop))
				self.circle = Circle(var_Circle)
				self.spindle = Spindle(var_Spindle)
				self.drop = Drop(var_Drop)


				super(Circle, self).__init__(circle)
				super(Spindle,self).__init__(spindle)
				super(Drop,self).__init__()


			class Circle(Spindle,Drop):

				def __init__(self, spindle, drop, bond=1, tiny_cell=6):

					self.bond1 = bond
					self.bond2 = bond
					self.bond3 = bond
					self.bond4 = bond
					self.bond5 = bond
					self.tiny_cell = tiny_cell
					self.star = Star(Circle(var_Circle),Spindle(var_Spindle),Drop(var_Drop))
					self.circle = Circle(var_Circle)
					self.spindle = Spindle(var_Spindle)
					self.drop = Drop(var_Drop)

					super(Spindle, self).__init__(spindle)	
					super(Drop, self).__init__()



				class Spindle(Drop):

					def __init__(self, bond=1, tiny_cell=6):

						self.bond1 = bond
						self.bond2 = bond
						self.bond3 = bond
						self.bond4 = bond
						self.bond5 = bond
						self.tiny_cell = tiny_cell
						self.star = Star(Circle(var_Circle),Spindle(var_Spindle),Drop(var_Drop))
						self.circle = Circle(var_Circle)
						self.spindle = Spindle(var_Spindle)
						self.drop = Drop(var_Drop)

						super(Drop, self).__init__()	

						
					class Drop():

						def __init__(self, bond=1, tiny_cell=6):

							self.bond1 = bond
							self.bond2 = bond
							self.bond3 = bond
							self.bond4 = bond
							self.bond5 = bond
							self.tiny_cell = tiny_cell
							self.star = Star(Circle(var_Circle),Spindle(var_Spindle),Drop(var_Drop))
							self.circle = Circle(var_Circle)
							self.spindle = Spindle(var_Spindle)
							self.drop = Drop(var_Drop)

						def relate_TinyCell(self, arg1):

							arg1.bond1 = self
							arg1.bond2 = self
							arg1.bond3 = self
							arg1.bond4 = self
							arg1.bond5 = self

							return arg1


						def create_the_shell1(self):

							var_Graph = Graph(20)
							var_vertex1 = AdjVertex(1)
							var_vertex2 = AdjVertex(2)
							var_vertex3 = AdjVertex(3)
							var_vertex4 = AdjVertex(4)
							var_vertex5 = AdjVertex(5)
							var_vertex6 = AdjVertex(6)
							var_vertex7 = AdjVertex(7)
							var_vertex8 = AdjVertex(8)
							var_vertex9 = AdjVertex(9)
							var_vertex10 = AdjVertex(10)
							var_vertex11 = AdjVertex(11)
							var_vertex12 = AdjVertex(12)
							var_vertex13 = AdjVertex(13)
							var_vertex14 = AdjVertex(14)
							var_vertex15 = AdjVertex(15)
							var_vertex16 = AdjVertex(16)
							var_vertex17 = AdjVertex(17)
							var_vertex18 = AdjVertex(18)
							var_vertex19 = AdjVertex(19)
							var_vertex20 = AdjVertex(20)


							var_Graph.add_edge_f1_1(var_vertex1, var_vertex2)
							var_Graph.add_edge_f1_1(var_vertex2, var_vertex3)
							var_Graph.add_edge_f1_1(var_vertex3, var_vertex9)
							var_Graph.add_edge_f1_1(var_vertex9, var_vertex15)
							var_Graph.add_edge_f1_1(var_vertex15, var_vertex20)

							var_Graph.add_edge_f1_1(var_vertex20, var_vertex19)
							var_Graph.add_edge_f1_1(var_vertex19, var_vertex18)
							var_Graph.add_edge_f1_1(var_vertex18, var_vertex12)
							var_Graph.add_edge_f1_1(var_vertex12, var_vertex6)
							var_Graph.add_edge_f1_1(var_vertex6, var_vertex1)


							var_Graph.add_edge_f1_1(var_vertex7, var_vertex8)
							var_Graph.add_edge_f1_1(var_vertex8, var_vertex14)
							var_Graph.add_edge_f1_1(var_vertex14, var_vertex13)
							var_Graph.add_edge_f1_1(var_vertex13, var_vertex7)

							var_Graph.add_edge_f1_1(var_vertex4, var_vertex5)
							var_Graph.add_edge_f1_1(var_vertex5, var_vertex10)
							var_Graph.add_edge_f1_1(var_vertex10, var_vertex4)

							var_Graph.add_edge_f1_1(var_vertex11, var_vertex17)
							var_Graph.add_edge_f1_1(var_vertex17, var_vertex16)
							var_Graph.add_edge_f1_1(var_vertex16, var_vertex11)


							return var_Graph


							
						def create_the_medium(self, arg, args_list):

							var_llist = LinkedList(arg)

							for item in args_list:

								var_llist.push(item)

							return var_llist


						def create_the_shell2(self):

							var_Graph = Graph(20)
							var_vertex1 = AdjVertex(1)
							var_vertex2 = AdjVertex(2)
							var_vertex3 = AdjVertex(3)
							var_vertex4 = AdjVertex(4)
							var_vertex5 = AdjVertex(5)
							var_vertex6 = AdjVertex(6)
							var_vertex7 = AdjVertex(7)
							var_vertex8 = AdjVertex(8)
							var_vertex9 = AdjVertex(9)
							var_vertex10 = AdjVertex(10)
							var_vertex11 = AdjVertex(11)
							var_vertex12 = AdjVertex(12)
							var_vertex13 = AdjVertex(13)
							var_vertex14 = AdjVertex(14)
							var_vertex15 = AdjVertex(15)
							var_vertex16 = AdjVertex(16)
							var_vertex17 = AdjVertex(17)
							var_vertex18 = AdjVertex(18)
							var_vertex19 = AdjVertex(19)
							var_vertex20 = AdjVertex(20)


							var_Graph.add_edge_f1_1(var_vertex1, var_vertex2)
							var_Graph.add_edge_f1_1(var_vertex2, var_vertex3)
							var_Graph.add_edge_f1_1(var_vertex3, var_vertex9)
							var_Graph.add_edge_f1_1(var_vertex9, var_vertex15)
							var_Graph.add_edge_f1_1(var_vertex15, var_vertex20)

							var_Graph.add_edge_f1_1(var_vertex20, var_vertex19)
							var_Graph.add_edge_f1_1(var_vertex19, var_vertex18)
							var_Graph.add_edge_f1_1(var_vertex18, var_vertex12)
							var_Graph.add_edge_f1_1(var_vertex12, var_vertex6)
							var_Graph.add_edge_f1_1(var_vertex6, var_vertex1)


							var_Graph.add_edge_f1_1(var_vertex7, var_vertex8)
							var_Graph.add_edge_f1_1(var_vertex8, var_vertex14)
							var_Graph.add_edge_f1_1(var_vertex14, var_vertex13)
							var_Graph.add_edge_f1_1(var_vertex13, var_vertex7)

							var_Graph.add_edge_f1_1(var_vertex4, var_vertex5)
							var_Graph.add_edge_f1_1(var_vertex5, var_vertex10)
							var_Graph.add_edge_f1_1(var_vertex10, var_vertex4)

							var_Graph.add_edge_f1_1(var_vertex11, var_vertex17)
							var_Graph.add_edge_f1_1(var_vertex17, var_vertex16)
							var_Graph.add_edge_f1_1(var_vertex16, var_vertex11)


							return var_Graph




						def relate_to_shell(self, shell1, medium, shell2):

							class Shell():

								def __init__(self, shell1, medium, shell2, bond=1):

									self.shell1 = shell1
									self.medium = medium
									self.shell2 = shell2
									self.bond1 = bond
									self.bond2 = bond


							var_shell = Shell(shell1, medium, shell2)

							return var_shell


						def bond_shell_to_shell(self, arg1, arg2):

							arg1.bond1 = arg2
							arg2.bond2 = arg1

							return self


						def create_the_CarbonNet(self, arg1, arg2):

							arg1.bond1 = arg2
							arg2.bond2 = arg1

							return self


		def create_TinyCell(self, circle, spindle, drop):

			return self.Star(circle, spindle, drop).Circle(spindle, drop).Spindle(drop).Drop()

		def relate_TinyCell_1(self, circle, spindle, drop, args_list):


			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0], args_list[1])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1], args_list[2])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[2], args_list[3])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[3], args_list[4])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[4], args_list[5])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[5], args_list[6])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[6], args_list[7])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[7], args_list[8])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[8], args_list[9])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[9], args_list[4])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[8], args_list[10])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[10], args_list[11])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[11], args_list[12])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[12], args_list[13])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[13], args_list[9])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[3], args_list[14])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[14], args_list[15])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[15], args_list[13])


			return (self, args_list)




		def relate_TinyCell_2(self, circle, spindle, drop, args_list):

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][0], args_list[1][1][0])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][0], args_list[2][1][0])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][1], args_list[1][1][1])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][1], args_list[2][1][1])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][2], args_list[1][1][2])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][2], args_list[2][1][2])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][3], args_list[1][1][3])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][3], args_list[2][1][3])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][4], args_list[1][1][4])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][4], args_list[2][1][4])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][5], args_list[1][1][5])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][5], args_list[2][1][5])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][6], args_list[1][1][6])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][6], args_list[2][1][6])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][7], args_list[1][1][7])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][7], args_list[2][1][7])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][8], args_list[1][1][8])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][8], args_list[2][1][8])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][9], args_list[1][1][9])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][9], args_list[2][1][9])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][10], args_list[1][1][10])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][10], args_list[2][1][10])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][11], args_list[1][1][11])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][11], args_list[2][1][11])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][12], args_list[1][1][12])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][12], args_list[2][1][12])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][13], args_list[1][1][13])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][13], args_list[2][1][13])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][14], args_list[1][1][14])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][14], args_list[2][1][14])

			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[0][1][15], args_list[1][1][15])
			self.create_TinyCell(circle,spindle,drop).bond_shell_to_shell(args_list[1][1][15], args_list[2][1][15])


			return (self, args_list)
