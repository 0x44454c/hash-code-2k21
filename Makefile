FILE = %
$(FILE): $(FILE).cc clean
	@time -f "\n%E - compilation" -a -o time.txt g++ $< -o $@ 
	@time -f "%E - execution" -a -o time.txt ./$@ 
	@cat time.txt
clean:
	@rm -rf $(FILE) time.txt
