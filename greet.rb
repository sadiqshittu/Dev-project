def greet(name)
    def get_user_input(prompt)
      print prompt
      gets.chomp
    end

    def assign_group
      ['A', 'B'].sample
    end

    def conduct_interview
      name = get_user_input("What's your name? ")
      job = get_user_input("What's your job? ")
      income = get_user_input("What's your income? ")
      
      puts "\nThank you for the information, #{name}."
      puts "Job: #{job}"
      puts "Income: #{income}"
      
      group = assign_group
      puts "\nYou have been assigned to Group #{group}."
      puts "I cannot explain the criteria for this assignment."
    end

    puts "Hello, #{name}!"
  end
  
  if __FILE__ == $0
    greet("USER")
  end
  