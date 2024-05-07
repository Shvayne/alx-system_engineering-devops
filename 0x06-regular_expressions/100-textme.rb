#!/usr/bin/env ruby

log_file = ARGV[0]

def extract_info(line)
  pattern = /[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/
  match_data = line.match(pattern)

  if match_data
    sender = match_data[:sender]
    receiver = match_data[:receiver]
    flags = match_data[:flags]
    return "#{sender},#{receiver},#{flags}"
  else
    return nil
  end
end

File.open(log_file, 'r') do |file|
  file.each_line do |line|
    info = extract_info(line)
    puts info if info
  end
end
