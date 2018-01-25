
#!/usr/bin/perl
use strict;
use warnings;

use REST::Client;
use MIME::Base64;
use JSON;
use Data::Dumper;

#allows JSON with boolean to display properly
$JSON::PP::true= "true";
$JSON::PP::false = "false";

# Configurables
my $endpoint = "https://10.0.0.30";
my $userpass = "apiuser:cisco"; #default username and password... can be reset by command line args
if( defined $ARGV[0] && defined $ARGV[1] ){ #check for command line args
    $userpass = $ARGV[0] . ":" . $ARGV[1];
}

# Older implementations of LWP check this to disable server verification
$ENV{PERL_LWP_SSL_VERIFY_HOSTNAME}=0;

# Set up the connection
my $client = REST::Client->new( );

# 2 ways of making a REST call are provided:
# One with "SSL verification turned off" and the other with "SSL verification turned on".
# The one with "SSL verification turned off" is commented out. If you like to use that then
# uncomment the line where SSL_verify_mode => 0 and comment the line with SSL_verify_mode => 1.
# Configuration to turn off SSL verification for a REST call:
$client->getUseragent()->ssl_opts( SSL_verify_mode => 0);
# Configuration to turn on SSL verification for a REST call: Download SSL certificates from your FMC and provide the downloaded path
# $client->getUseragent()->ssl_opts( SSL_verify_mode => 1 , SSL_ca_file => 'path/to/ssl_certificate');

$client->setHost( $endpoint );
$client->addHeader( "Authorization", "Basic ".encode_base64( $userpass ) );
$client->addHeader( "Content-Type", "application/json");

#Generating auth token
my $auth_url = "/api/fmc_platform/v1/auth/generatetoken";
$client->POST($auth_url);
my $auth_token = $client->responseHeader('X-auth-access-token');
$client->addHeader("X-auth-access-token",$auth_token);
my $api_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords"; #param
my $last_char = substr($api_url,-1);
if ($last_char eq '/'){
    chop($api_url);
}



# Perform a HTTP POST on this URI
my $data = '{
  "name": "vFTD1",
  "hostName": "10.0.0.51",
  "natID": "",
  "regKey": "cisco123",
  "type": "Device",
  "license_caps": [
    "BASE",
    "MALWARE",
    "URLFilter",
    "THREAT"
  ],
  "accessPolicy": {
    "name": "ftd-policy",
    "type": "AccessPolicy"
  }
}';
$client->POST( $api_url, $data );
print $client->responseContent();


#decode and print json response
print "Response code: ";
print $client->responseCode();
print "\n";

my $respText = $client->responseContent();
if ($respText) {
    my $resp = decode_json( $client->responseContent() );
    print Dumper($resp);
}
print "Now sleep 15sec before trying to register FTD2....\n";
sleep(15);

# FTD2 registartion
# Perform a HTTP POST on this URI
$data = '{
  "name": "vFTD2",
  "hostName": "10.0.0.52",
  "natID": "",
  "regKey": "cisco123",
  "type": "Device",
  "license_caps": [
    "BASE",
    "MALWARE",
    "URLFilter",
    "THREAT"
  ],
  "accessPolicy": {
    "name": "ftd-policy",
    "type": "AccessPolicy"
  }
}';
$client->POST( $api_url, $data );
print $client->responseContent();


#decode and print json response
print "Response code: ";
print $client->responseCode();
print "\n";

$respText = $client->responseContent();
if ($respText) {
    my $resp = decode_json( $client->responseContent() );
    print Dumper($resp);
}

