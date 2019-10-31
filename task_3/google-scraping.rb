require 'nokogiri'
require 'open-uri'
#open uri is a gem which allows to interact with web pages 
puts 'enter your query'
question = gets
url = open('https://www.google.com/search?q=' + question)
#opens the given word in google
content = Nokogiri::HTML(url)
#parses the html content from google
content.xpath('(//div/a/div[text()])').each do |give|
	puts give.content
end