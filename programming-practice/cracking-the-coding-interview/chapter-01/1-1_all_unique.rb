def string_has_all_unique_chars?(str)
  char_set = Array.new(256, false)
  str.each_char do |c|
    return false if char_set[c.ord]
    char_set[c.ord] = true
  end
  true
end

def main()
   str_1 = "abcdefghijk"
   str_2 = "a"*3
   
   puts "#{str_1} has all unique_characters => #{string_has_all_unique_chars?(str_1)}"
   puts "#{str_2} has all unique_characters => #{string_has_all_unique_chars?(str_2)}"
end

main()