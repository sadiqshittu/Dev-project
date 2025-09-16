def greet(name)
    puts "Hello, #{name}!"
  end
  
  if __FILE__ == $0
    greet("USER")
  end
  