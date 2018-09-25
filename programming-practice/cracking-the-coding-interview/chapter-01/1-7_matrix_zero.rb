=begin
If we do a normal iteration and set zeros to a row and column, in the next iteration
that row and column will be seen as zero by our code and ultimately entire row and column
will be set to zero.
To avoid this, first we mark all the rows that have zero and all columns that have zero.
then we use the marked rows and columns to set zeros.
=end

require "test/unit"

class ReplaceRowsAndColumnsOfAMatrixWithZero
  def initialize(matrix, row_count, col_count)
    @matrix = matrix
    @row_count = row_count
    @col_count = col_count
    @row = Array.new @row_count, false
    @column = Array.new @col_count, false
  end
  
  def replace
    mark_zeros_in_matrix
    replace_with_zero
  end
  
  private
  def replace_with_zero
    0.upto(@row_count-1) do |i|
      0.upto(@col_count-1) do |j|
        if @row[i] or @column[j]
          @matrix[i][j] = 0
        end
      end
    end
    @matrix
  end
  
  def mark_zeros_in_matrix
    0.upto(@row_count-1) do |i|
      0.upto(@col_count-1) do |j|
        if @matrix[i][j] == 0
          @row[i] = true
          @column[j] = true
        end
      end
    end
  end
end

class TestReplaceRowsAndColumnsOfAMatrixWithZero < Test::Unit::TestCase
  def setup
    #pass
  end
  
  def teardown
    #pass
  end
  
  def test_replace
    matrix = [[1,2,3], [4, 0, 6], [7,8,9]]
    row_count = 3
    col_count = 3
    r = ReplaceRowsAndColumnsOfAMatrixWithZero.new(matrix, row_count, col_count)
    m = r.replace
    
    assert_equal(m[0][0], matrix[0][0])
    assert_equal(m[0][1], 0)
    assert_equal(m[0][2], matrix[0][2])
  
    assert_equal(m[1][0], 0)
    assert_equal(m[1][1], 0)
    assert_equal(m[1][2], 0)
    
    assert_equal(m[2][0], matrix[2][0])
    assert_equal(m[2][1], 0)
    assert_equal(m[2][2], matrix[2][2])

  end
end
