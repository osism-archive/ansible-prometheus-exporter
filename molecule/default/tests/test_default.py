def test_node_exporter_file(host):
    f = host.file("/usr/sbin/node_exporter")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
