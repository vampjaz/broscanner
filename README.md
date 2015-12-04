## BroScanner:
### python streaming scanner for bro logfiles

dependencies
- python 2.7
- my version of pytailer: https://github.com/red-green/pytailer
- bro
- pync for OSX notifications (more coming soon)








notes... (not all files listed here)

```
$ head -n20 * | grep -e "==>" -e "#fields" -e "#types"
==> communication.log <==
#fields	ts	peer	src_name	connected_peer_desc	connected_peer_addr	connected_peer_porlevel	message
#types	time	string	string	string	addr	port	string	string
==> conn.log <==
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents
#types	time	string	addr	port	addr	port	enum	string	interval	count	count	string	bool	bool	count	string	count	count	count	count	set[string]
==> dhcp.log <==
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	mac	assigned_ilease_time	trans_id
#types	time	string	addr	port	addr	port	string	addr	interval	count
==> dns.log <==
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	trans_id	query	qclass	qclass_name	qtype	qtype_name	rcode	rcode_name	AA	TC	RD	RAanswers	TTLs	rejected
#types	time	string	addr	port	addr	port	enum	count	string	count	string	count	string	count	string	bool	bool	bool	bool	count	vector[string]	vector[interval]	bool
==> files.log <==
#fields	ts	fuid	tx_hosts	rx_hosts	conn_uids	source	depth	analyzers	mime_type	filename	duration	local_orig	is_orig	seen_bytes	total_bytes	missing_bytes	overflow_bytes	timedout	parent_fuid	md5	sha1	sha256	extracted
#types	time	string	set[addr]	set[addr]	set[string]	string	count	set[string]	string	string	interval	bool	bool	count	count	count	count	bool	string	string	string	string	string
==> http.log <==
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	trans_depth	method	host	uri	referrer	user_agent	request_body_len	response_body_len	status_code	status_msg	info_code	info_msg	filename	tags	username	password	proxied	orig_fuids	orig_mime_types	resp_fuids	resp_mime_types
#types	time	string	addr	port	addr	port	count	string	string	string	string	string	count	count	count	string	count	string	string	set[enum]	string	string	set[string]	vector[string]	vector[string]	vector[string]	vector[string]
==> known_hosts.log <==
#fields	ts	host
#types	time	addr
==> known_services.log <==
#fields	ts	host	port_num	port_proto	service
#types	time	addr	port	enum	set[string]
==> loaded_scripts.log <==
#fields	name
#types	string
==> packet_filter.log <==
#fields	ts	node	filter	init	success
#types	time	string	string	bool	bool
==> software.log <==
#fields	ts	host	host_p	software_type	name	version.major	version.minor	version.minor2	version.minor3	version.addl	unparsed_version
#types	time	addr	port	enum	string	count	count	count	count	string	string
==> ssl.log <==
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	version	cipher	curve	server_name	resumed	last_alert	next_protocol	established	cert_chain_fuids	client_cert_chain_fuids	subject	issuer	client_subject	client_issuer	validation_status
#types	time	string	addr	port	addr	port	string	string	string	string	bool	string	string	bool	vector[string]	vector[string]	string	string	string	string	string
==> stderr.log <==
==> stdout.log <==
==> weird.log <==
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	name	addl	notice	peer
#types	time	string	addr	port	addr	port	string	string	bool	string
==> x509.log <==
#fields	ts	id	certificate.version	certificate.serial	certificate.subject	certificate.issuer	certificate.not_valid_before	certificate.not_valid_after	certificate.key_alg	certificate.sig_alg	certificate.key_type	certificate.key_length	certificate.exponent	certificate.curve	san.dns	san.uri	san.email	san.ip	basic_constraints.ca	basic_constraints.path_len
#types	time	string	count	string	string	string	time	time	string	string	string	count	string	string	vector[string]	vector[string]	vector[string]	vector[addr]	bool	count
```
