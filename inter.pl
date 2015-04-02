use strict;
use warnings;

open(my $in, "<", "output.txt") or die "Can't open text file";
open(my $out, ">>", "data.txt") or die "Can't make new text file";

my $i = 0;
my @links;
my $link_count = 0;
while(<$in>)
{	
	if($i==0)
	{
		print $out $_."\t";
	}
	else
	{}
	if(/http:\/\/tp.iitkgp/)
	{
		$links[$link_count] = $_;
		$link_count++;
	}			
	else
	{}
	#Try some spatially local regular expressions.
	if(/rs\.*\w*(\d+\.*\,*\d+\.*\,*\d+\.*\,*)/)
	{
		print $_;	
	}



	$i++;
}
#Links are successfully extracted.
foreach(@links) {
	print $_;
}
