objs =  multiplication.o division.o addition.o subtraction.o main.o 

calculator: $(objs) operations.h
	cc -o calculator $(objs)

$(objs): %.o:%.c
	cc -c $< -o $@

clean:
	rm -f calculator $(objs)

.PHONY: clean
