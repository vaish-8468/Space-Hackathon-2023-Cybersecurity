#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser.NuLog import NuLogParser


input_dir  = '../logs/Bhuvan/' # The input directory of log file
output_dir = 'NuLogParser_result/' # The output directory of parsing results
log_file   = input_dir+'nonAnomalous (1).log' # The input log file name
log_format = '<IPAddress> <UserLogin> <UserAuth> <DateTime> <Content> <HTTPStatusCode> <BytesSent> <Component> <UserAgent> <Data>'
# rsupport   = 10 # The minimum threshold of relative support, 10 denotes 10%
regex      = r'\s+' # Regular expression list for optional preprocessing (default: [])
template_filepath = log_file + '_templates.csv' # The event template file path
nr_epochs=15
num_samples=0

# parser = NuLogParser.LogParser(input_dir, log_format, output_dir, rsupport=rsupport)
# parser.parse(log_file)
parser = NuLogParser.LogParser(indir=input_dir, outdir=output_dir,log_format=log_format)
parser.parse(log_file, nr_epochs=nr_epochs, num_samples=num_samples)
