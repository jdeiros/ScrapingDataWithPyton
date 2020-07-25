import email_sender as es
import scrape_html_dolarhoy as dh

sender = es.EmailSender(dh.getDolarCurrentQuote())
sender.send()

