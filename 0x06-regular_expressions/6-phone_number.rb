#!/usr/bin/env ruby
# Regular expression to match 10 digit number
puts ARGV[0].scan(/^[0-9]{10}$/).join
