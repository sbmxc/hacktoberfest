// Hello World, in Verilog! 
// @author igu9

module helloWorld ;
  
initial begin
	$display ("Hello, World! by igu9");
	#10  $finish;
end
  
endmodule // End of Module helloWorld