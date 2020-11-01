#!/usr/bin/env perl
use 5.20.0;  # enables warning and strict pragma

# allow unicode in strings
use utf8;

# encode output as utf-8 on std filehandles
# without this you would see "wide character" warnings
use open ':std', ':encoding(UTF-8)';

say "Hello World";      # plain string is still unicode with `use utf8`
say "Hello \x{1F30D}";  # unicode escape sequence
say "Hello 🌍";         # unicode char in file
