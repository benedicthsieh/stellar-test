import re


def parse_kv_pairs(subline):
    m = re.findall("[^=]*='[^=]*'", subline)
    pairs = [p.strip().split('=') for p in m]
    return pairs

def parse_line(line):
    ts = line[0:28]
    subline = line[29:]
    return ts, parse_kv_pairs(subline)

def scrub_dob_from_pairs(pairs, line):
    for pair in pairs:
        if pair[0] == 'DOB':
            dob_split = pair[1].split('/')
            if len(dob_split) != 3:
                print('Could not fully parse log line: ', line)
                print('Rewriting DOB to \'\'')
                pair[1] = "''"
            else:
                # TODO: we didn't quite parse the string cleanly, adding the leading ' back in
                # is a hack we should fix.
                pair[1] = "'X/X/{}".format(dob_split[2])

def format_kv_pairs(pairs):
    #print('pairs', pairs)
    out_pairs = ['{}={}'.format(k,v) for (k,v) in pairs]
    return ' '.join(out_pairs)

def format_line(ts, pairs):
    return ts + ' ' + format_kv_pairs(pairs)

def scrub_line(line):
    (ts, pairs) = parse_line(line)
    scrub_dob_from_pairs(pairs, line)
    return format_line(ts, pairs)
