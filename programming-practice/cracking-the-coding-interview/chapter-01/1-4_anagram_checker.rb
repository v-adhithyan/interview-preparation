def anagram?(str1, str2)
  char_set = Array.new 256, 0
  str1.each_char.map {|c| char_set[c.ord] = char_set[c.ord] + 1}
  unique_chars = char_set.select {|num| num > 0}
  unique_chars = unique_chars.count
  completed_chars = 0
  str2.each_char.with_index do |c, i|
    return false if char_set[c.ord] == 0
    char_set[c.ord] -= 1
    
    if char_set[c.ord] == 0
      completed_chars += 1
      return true if (completed_chars == unique_chars) and (i == str2.length - 1)
    end
  end
  false
end

def main()
  puts "brainy and binary are anagrams => #{anagram?("brainy", "binary")}"
  puts "rat and act are anagrams => #{anagram?("rat", "act")}"
  puts "adhithyan and vijayakumar are anagrams => #{anagram?("adhithyan", "vijayakumar")}"
end

main()