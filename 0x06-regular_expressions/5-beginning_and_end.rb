#!/usr/bin/env ruby
# Regular expression to match string starting with h and ending with n
puts ARGV[0].scan(/h.n/).join
