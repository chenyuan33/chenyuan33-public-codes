my $in = <STDIN>;
chomp $in;
$in = [split /[\s,]+/, $in];
my $c = $in->[0] + $in->[1];
print "$c\n";
