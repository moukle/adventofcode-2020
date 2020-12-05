#!/usr/bin/env julia

input = open("./input1.txt") do file
	lines = readlines(file)
	parse.(Int, lines)
end


function solve_1()
	for a in input, b in input
		if a + b == 2020
			println(a*b)
			return
		end
	end
end

function solve_2()
	for a in input, b in input, c in input
		if a + b + c == 2020
			println(a*b*c)
			return
		end
	end
end

solve_1()
solve_2()
