import base64

with open('/nfs/103214813/temp/logo_b64.txt', 'r') as f:
    logo_b64 = f.read()
with open('/nfs/103214813/temp/bg_b64.txt', 'r') as f:
    bg_b64 = f.read()
with open('/nfs/103214813/temp/ico_b64.txt', 'r') as f:
    ico_b64 = f.read()

def section(id, title, icon, content):
    return f'''
        <div class="section-page" id="sec-{id}" style="display:none">
            <div class="section-title"><i class="fas fa-{icon}"></i> {title}</div>
            {content}
        </div>'''

def form_row(label, inp):
    return f'<div class="form-row"><label>{label}</label>{inp}</div>'

def data_table(headers, rows):
    h = ''.join(f'<th>{x}</th>' for x in headers)
    body = ''
    for r in rows:
        body += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return f'<table class="data-table"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'

sections = []

# ── Início (home) ──
sections.append(section('inicio', 'Início', 'home', '''
    <div class="widgets-row">
        <div class="widget-card"><div class="widget-icon purple"><i class="fas fa-server"></i></div><div class="widget-number">5</div><div class="widget-label">Servidores CS</div></div>
        <div class="widget-card"><div class="widget-icon green"><i class="fas fa-users"></i></div><div class="widget-number">127</div><div class="widget-label">Usuários Ativos</div></div>
        <div class="widget-card"><div class="widget-icon orange"><i class="fas fa-wifi"></i></div><div class="widget-number">34</div><div class="widget-label">Online Agora</div></div>
        <div class="widget-card"><div class="widget-icon red"><i class="fas fa-key"></i></div><div class="widget-number">312</div><div class="widget-label">Linhas Ativas</div></div>
    </div>
    <div class="info-grid">
        <div class="panel"><div class="panel-header"><i class="fas fa-server"></i> Status dos Servidores</div><div class="panel-body">
            <div class="server-status-grid">
                <div class="server-box"><div class="status-dot online"></div><div class="sv-name">CCCam-01</div><div class="sv-info">12000 | 87 users</div><span class="sv-badge online">Online</span></div>
                <div class="server-box"><div class="status-dot online"></div><div class="sv-name">CCCam-02</div><div class="sv-info">12000 | 63 users</div><span class="sv-badge online">Online</span></div>
                <div class="server-box"><div class="status-dot online"></div><div class="sv-name">MGcamd-01</div><div class="sv-info">15000 | 28 users</div><span class="sv-badge online">Online</span></div>
                <div class="server-box"><div class="status-dot online"></div><div class="sv-name">Newcamd-01</div><div class="sv-info">16000 | 15 users</div><span class="sv-badge online">Online</span></div>
                <div class="server-box"><div class="status-dot online"></div><div class="sv-name">OSCam-01</div><div class="sv-info">9000 | 42 users</div><span class="sv-badge online">Online</span></div>
                <div class="server-box"><div class="status-dot offline"></div><div class="sv-name">CSP-01</div><div class="sv-info">8000 | 0 users</div><span class="sv-badge offline">Offline</span></div>
            </div>
        </div></div>
        <div class="panel"><div class="panel-header"><i class="fas fa-key"></i> Minhas Linhas</div><div class="panel-body">
            <div class="cline-box"><span class="cline-label">C-Line</span><span class="cline-value">C: cs1.homerfull.net 12000 usuario01 senhaX4k</span><span class="copy-btn" onclick="copyLine(this)">Copiar</span></div>
            <div class="cline-box"><span class="cline-label">MG-Line</span><span class="cline-value">MG: cs1.homerfull.net 15000 usuario01 senhaM2q</span><span class="copy-btn" onclick="copyLine(this)">Copiar</span></div>
            <div class="cline-box"><span class="cline-label">N-LINE</span><span class="cline-value">N: cs1.homerfull.net 16000 usuario01 senhaN5w 01 02 03 04 05 10 11 12 13 14</span><span class="copy-btn" onclick="copyLine(this)">Copiar</span></div>
        </div></div>
    </div>
    <div class="panel"><div class="panel-header"><i class="fas fa-users"></i> Usuários CS - Linhas Recentes</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Usuário','Protocolo','Servidor','Conexões','Validade','Status'],
        [['1','<i class="fas fa-user" style="color:#6967CE;margin-right:5px"></i>cliente01','<span class="proto-tag proto-cccam"><i class="fas fa-satellite-dish"></i> CCCam</span>','CCCam-01','1','15/09/2026','<span class="badge-status badge-active">Ativo</span>'],
         ['2','<i class="fas fa-user" style="color:#6967CE;margin-right:5px"></i>cliente02','<span class="proto-tag proto-cccam"><i class="fas fa-satellite-dish"></i> CCCam</span>','CCCam-02','2','20/09/2026','<span class="badge-status badge-active">Ativo</span>'],
         ['3','<i class="fas fa-user" style="color:#6967CE;margin-right:5px"></i>revenda_norte','<span class="proto-tag proto-mgcamd"><i class="fas fa-broadcast-tower"></i> MGcamd</span>','MGcamd-01','5','01/12/2026','<span class="badge-status badge-active">Ativo</span>'],
         ['4','<i class="fas fa-user" style="color:#6967CE;margin-right:5px"></i>teste_sp','<span class="proto-tag proto-newcamd"><i class="fas fa-satellite"></i> Newcamd</span>','Newcamd-01','1','18/08/2026','<span class="badge-status badge-test">Teste</span>'],
         ['5','<i class="fas fa-user" style="color:#75798f;margin-right:5px"></i>cliente05','<span class="proto-tag proto-cccam"><i class="fas fa-satellite-dish"></i> CCCam</span>','CCCam-01','1','10/08/2026','<span class="badge-status badge-expired">Expirado</span>'],
         ['6','<i class="fas fa-user" style="color:#6967CE;margin-right:5px"></i>revenda_sul','<span class="proto-tag proto-occam"><i class="fas fa-microchip"></i> OSCam</span>','OSCam-01','10','30/11/2026','<span class="badge-status badge-active">Ativo</span>']]) + '''</div></div>
    <div class="panel"><div class="panel-header"><i class="fas fa-wifi"></i> Conexões Online Agora</div><div class="panel-body" style="padding:0">
        ''' + data_table(['Usuário','IP','Protocolo','Servidor','Uptime','Hops','Status'],
        [['cliente01','189.xxx.xxx.42','<span class="proto-tag proto-cccam"><i class="fas fa-satellite-dish"></i> CCCam</span>','CCCam-01','4h 23m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['cliente02','200.xxx.xxx.15','<span class="proto-tag proto-cccam"><i class="fas fa-satellite-dish"></i> CCCam</span>','CCCam-02','1h 10m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['revenda_norte','177.xxx.xxx.88','<span class="proto-tag proto-mgcamd"><i class="fas fa-broadcast-tower"></i> MGcamd</span>','MGcamd-01','12h 05m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['revenda_sul','150.xxx.xxx.201','<span class="proto-tag proto-occam"><i class="fas fa-microchip"></i> OSCam</span>','OSCam-01','8h 47m','Hop1','<span class="badge-status badge-connected">Conectado</span>']]) + '''</div></div>
    <div class="panel"><div class="panel-header"><i class="fas fa-tachometer-alt"></i> Recursos do Servidor</div><div class="panel-body">
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
            <div style="background:#f7f5ff;padding:18px;border-radius:10px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><i class="fas fa-hdd" style="font-size:20px;color:#6967CE"></i><span style="font-size:12px;color:#75798f;font-weight:700">DISCO</span></div><div style="font-size:22px;font-weight:700;color:#404666;font-family:Comfortaa">45 GB <span style="font-size:12px;color:#75798f">/ 100 GB</span></div><div class="progress-bar"><div class="progress-fill purple" style="width:45%"></div></div></div>
            <div style="background:#f7f5ff;padding:18px;border-radius:10px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><i class="fas fa-memory" style="font-size:20px;color:#6967CE"></i><span style="font-size:12px;color:#75798f;font-weight:700">MEMÓRIA</span></div><div style="font-size:22px;font-weight:700;color:#404666;font-family:Comfortaa">5.4 GB <span style="font-size:12px;color:#75798f">/ 8 GB</span></div><div class="progress-bar"><div class="progress-fill orange" style="width:67%"></div></div></div>
            <div style="background:#f7f5ff;padding:18px;border-radius:10px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><i class="fas fa-microchip" style="font-size:20px;color:#6967CE"></i><span style="font-size:12px;color:#75798f;font-weight:700">CPU</span></div><div style="font-size:22px;font-weight:700;color:#404666;font-family:Comfortaa">38%</div><div class="progress-bar"><div class="progress-fill green" style="width:38%"></div></div></div>
        </div>
        <div style="margin-top:15px;display:grid;grid-template-columns:repeat(2,1fr);gap:15px">
            <div style="display:flex;align-items:center;gap:10px;padding:12px;background:#fbfaff;border-radius:8px;border:1px solid #e2d8ff"><i class="fas fa-network-wired" style="font-size:18px;color:#32cafe"></i><div><div style="font-size:11px;color:#75798f">BANDA LARGA</div><div style="font-size:15px;font-weight:700;color:#404666">245 Mbps</div></div></div>
            <div style="display:flex;align-items:center;gap:10px;padding:12px;background:#fbfaff;border-radius:8px;border:1px solid #e2d8ff"><i class="fas fa-satellite" style="font-size:18px;color:#9f78ff"></i><div><div style="font-size:11px;color:#75798f">UPTIME SERVIDOR</div><div style="font-size:15px;font-weight:700;color:#404666">47d 12h 33m</div></div></div>
        </div>
    </div><div class="panel-footer">HomerFull CS Panel v3.0 &copy; 2026</div></div>'''))

# ── CCCam sections ──
sections.append(section('cccam-add', 'Adicionar Servidor CCCam', 'plus-circle', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-plus-circle"></i> Novo Servidor CCCam</div><div class="panel-body">
        ''' + form_row('Nome do Servidor', '<input type="text" placeholder="Ex: CCCam-03">') + '''
        ''' + form_row('IP / Host', '<input type="text" placeholder="Ex: 192.168.1.100 ou cs3.homerfull.net">') + '''
        ''' + form_row('Porta CCCam', '<input type="number" placeholder="12000" value="12000">') + '''
        ''' + form_row('Usuário', '<input type="text" placeholder="admin">') + '''
        ''' + form_row('Senha', '<input type="password" placeholder="********">') + '''
        ''' + form_row('Max. Usuários', '<input type="number" placeholder="100" value="100">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Criar Servidor CCCam</button>
    </div></div>'''))

sections.append(section('cccam-list', 'Listar Servidores CCCam', 'list', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-list"></i> Servidores CCCam</div><div class="panel-body" style="padding:0">
        ''' + data_table(['Servidor','Host','Porta','Usuários','Status','Ações'],
        [['CCCam-01','cs1.homerfull.net','12000','87/100','<span class="badge-status badge-active">Online</span>','<span class="copy-btn" style="padding:4px 10px;font-size:10px">Editar</span> <span class="copy-btn" style="padding:4px 10px;font-size:10px;background:#dc3545">Deletar</span>'],
         ['CCCam-02','cs2.homerfull.net','12000','63/100','<span class="badge-status badge-active">Online</span>','<span class="copy-btn" style="padding:4px 10px;font-size:10px">Editar</span> <span class="copy-btn" style="padding:4px 10px;font-size:10px;background:#dc3545">Deletar</span>'],
         ['CCCam-BK','cs-bk.homerfull.net','12000','0/50','<span class="badge-status badge-expired">Offline</span>','<span class="copy-btn" style="padding:4px 10px;font-size:10px">Editar</span> <span class="copy-btn" style="padding:4px 10px;font-size:10px;background:#dc3545">Deletar</span>']]) + '''</div></div>'''))

sections.append(section('cccam-clines', 'Gerar C-Lines CCCam', 'key', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-key"></i> Gerar C-Lines</div><div class="panel-body">
        ''' + form_row('Servidor', '<select><option>CCCam-01</option><option>CCCam-02</option></select>') + '''
        ''' + form_row('Usuário', '<input type="text" placeholder="nome_usuario">') + '''
        ''' + form_row('Senha', '<input type="text" placeholder="senha_aleatoria">') + '''
        ''' + form_row('Validade', '<select><option>30 dias</option><option>90 dias</option><option>180 dias</option><option>365 dias</option></select>') + '''
        ''' + form_row('Max. Conexões', '<input type="number" value="1">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Gerar C-Line</button>
        <div style="margin-top:20px">
            <div class="cline-box"><span class="cline-label">C-Line</span><span class="cline-value">C: cs1.homerfull.net 12000 user_new passX8k</span><span class="copy-btn" onclick="copyLine(this)">Copiar</span></div>
        </div>
    </div></div>'''))

sections.append(section('cccam-restart', 'Restart CCCam', 'sync-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-sync-alt"></i> Reiniciar Serviço CCCam</div><div class="panel-body">
        <p style="margin-bottom:15px;color:#75798f">Selecione o servidor para reiniciar o serviço CCCam:</p>
        ''' + form_row('Servidor', '<select><option>CCCam-01</option><option>CCCam-02</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px;background:linear-gradient(to right,#dc3545,#c82333)">⚠ Reiniciar CCCam</button>
        <div style="margin-top:15px;padding:15px;background:#d4edda;border-radius:8px;color:#155724;font-size:13px;display:none" id="restart-ok">✓ Serviço CCCam reiniciado com sucesso!</div>
    </div></div>'''))

# ── MGcamd sections ──
sections.append(section('mgcamd-add', 'Adicionar Servidor MGcamd', 'plus-circle', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-plus-circle"></i> Novo Servidor MGcamd</div><div class="panel-body">
        ''' + form_row('Nome do Servidor', '<input type="text" placeholder="Ex: MGcamd-02">') + '''
        ''' + form_row('IP / Host', '<input type="text" placeholder="Ex: 192.168.1.101">') + '''
        ''' + form_row('Porta MGcamd', '<input type="number" placeholder="15000" value="15000">') + '''
        ''' + form_row('Deskey', '<input type="text" placeholder="01 02 03 04 05 10 11 12 13 14" value="01 02 03 04 05 10 11 12 13 14">') + '''
        ''' + form_row('Max. Usuários', '<input type="number" value="80">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Criar Servidor MGcamd</button>
    </div></div>'''))

sections.append(section('mgcamd-list', 'Listar Servidores MGcamd', 'list', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-list"></i> Servidores MGcamd</div><div class="panel-body" style="padding:0">
        ''' + data_table(['Servidor','Host','Porta','Usuários','Status','Ações'],
        [['MGcamd-01','cs1.homerfull.net','15000','28/80','<span class="badge-status badge-active">Online</span>','<span class="copy-btn" style="padding:4px 10px;font-size:10px">Editar</span>'],
         ['MGcamd-02','cs2.homerfull.net','15000','0/60','<span class="badge-status badge-expired">Offline</span>','<span class="copy-btn" style="padding:4px 10px;font-size:10px">Editar</span>']]) + '''</div></div>'''))

sections.append(section('mgcamd-lines', 'Gerar MG-Lines', 'key', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-key"></i> Gerar MG-Lines</div><div class="panel-body">
        ''' + form_row('Servidor', '<select><option>MGcamd-01</option><option>MGcamd-02</option></select>') + '''
        ''' + form_row('Usuário', '<input type="text" placeholder="nome_usuario">') + '''
        ''' + form_row('Senha', '<input type="text" placeholder="senha">') + '''
        ''' + form_row('Validade', '<select><option>30 dias</option><option>90 dias</option><option>180 dias</option><option>365 dias</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Gerar MG-Line</button>
        <div style="margin-top:20px"><div class="cline-box"><span class="cline-label">MG-Line</span><span class="cline-value">MG: cs1.homerfull.net 15000 user_mg passM3k</span><span class="copy-btn" onclick="copyLine(this)">Copiar</span></div></div>
    </div></div>'''))

# ── Newcamd sections ──
sections.append(section('newcamd-add', 'Adicionar Servidor Newcamd', 'plus-circle', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-plus-circle"></i> Novo Servidor Newcamd</div><div class="panel-body">
        ''' + form_row('Nome do Servidor', '<input type="text" placeholder="Ex: Newcamd-02">') + '''
        ''' + form_row('IP / Host', '<input type="text" placeholder="Ex: 192.168.1.102">') + '''
        ''' + form_row('Porta Newcamd', '<input type="number" placeholder="16000" value="16000">') + '''
        ''' + form_row('Deskey', '<input type="text" placeholder="01 02 03 04 05 10 11 12 13 14" value="01 02 03 04 05 10 11 12 13 14">') + '''
        ''' + form_row('Max. Usuários', '<input type="number" value="60">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Criar Servidor Newcamd</button>
    </div></div>'''))

sections.append(section('newcamd-list', 'Listar Servidores Newcamd', 'list', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-list"></i> Servidores Newcamd</div><div class="panel-body" style="padding:0">
        ''' + data_table(['Servidor','Host','Porta','Deskey','Usuários','Status'],
        [['Newcamd-01','cs1.homerfull.net','16000','01 02 03...14','15/60','<span class="badge-status badge-active">Online</span>'],
         ['Newcamd-BK','cs-bk.homerfull.net','16000','01 02 03...14','0/40','<span class="badge-status badge-expired">Offline</span>']]) + '''</div></div>'''))

sections.append(section('newcamd-lines', 'Gerar N-Lines', 'key', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-key"></i> Gerar N-Lines</div><div class="panel-body">
        ''' + form_row('Servidor', '<select><option>Newcamd-01</option></select>') + '''
        ''' + form_row('Usuário', '<input type="text" placeholder="nome_usuario">') + '''
        ''' + form_row('Senha', '<input type="text" placeholder="senha">') + '''
        ''' + form_row('Validade', '<select><option>30 dias</option><option>90 dias</option><option>365 dias</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Gerar N-LINE</button>
        <div style="margin-top:20px"><div class="cline-box"><span class="cline-label">N-LINE</span><span class="cline-value">N: cs1.homerfull.net 16000 user_nc passN7w 01 02 03 04 05 10 11 12 13 14</span><span class="copy-btn" onclick="copyLine(this)">Copiar</span></div></div>
    </div></div>'''))

# ── OSCam ──
sections.append(section('oscam', 'Servidor OSCam', 'microchip', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-microchip"></i> OSCam - Configuração</div><div class="panel-body">
        <div class="server-box" style="margin-bottom:15px"><div class="status-dot online"></div><div class="sv-name">OSCam-01</div><div class="sv-info">Porta 9000 | 42 users | Hop1</div><span class="sv-badge online">Online</span></div>
        <h4 style="margin:15px 0 10px;color:#6967CE">Configuração OSCam</h4>
        <div class="cline-box"><span class="cline-label">Reader</span><span class="cline-value" style="font-family:monospace;font-size:11px">[reader]<br>label = homerfull<br>protocol = cccam<br>device = cs1.homerfull.net,12000<br>user = oscam_user<br>password = oscam_pass<br>group = 1</span></div>
        ''' + form_row('Web Interface Porta', '<input type="number" value="8888">') + '''
        ''' + form_row('Log Level', '<select><option>Normal</option><option>Debug</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Config</button>
    </div></div>'''))

# ── CSP ──
sections.append(section('csp', 'Servidor CSP', 'network-wired', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-network-wired"></i> CSP - Card Sharing Proxy</div><div class="panel-body">
        <div class="server-box" style="margin-bottom:15px"><div class="status-dot offline"></div><div class="sv-name">CSP-01</div><div class="sv-info">Porta 8000 | 0 users</div><span class="sv-badge offline">Offline</span></div>
        <div style="padding:15px;background:#fff3cd;border-radius:8px;color:#856404;font-size:13px;margin-bottom:15px">⚠ Servidor CSP está offline. Verifique a conexão e reinicie o serviço.</div>
        ''' + form_row('CSP Proxy Host', '<input type="text" value="csp.homerfull.net">') + '''
        ''' + form_row('Porta CSP', '<input type="number" value="8000">') + '''
        ''' + form_row('Profile', '<select><option>default</option><option>backup</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px;background:linear-gradient(to right,#ffc107,#fd7e14)">Iniciar CSP</button>
    </div></div>'''))

# ── Gerenciar ──
sections.append(section('admin', 'Administrador', 'shield-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-shield-alt"></i> Gerenciar Administradores</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Usuário','Email','Nível','Status'],
        [['1','admin','admin@homerfull.com','Super Admin','<span class="badge-status badge-active">Ativo</span>'],
         ['2','admin2','admin2@homerfull.com','Admin','<span class="badge-status badge-active">Ativo</span>'],
         ['3','suporte','suporte@homerfull.com','Moderador','<span class="badge-status badge-active">Ativo</span>']]) + '''</div></div>
    <div class="panel"><div class="panel-header"><i class="fas fa-plus-circle"></i> Adicionar Admin</div><div class="panel-body">
        ''' + form_row('Usuário', '<input type="text" placeholder="novo_admin">') + '''
        ''' + form_row('Email', '<input type="email" placeholder="email@exemplo.com">') + '''
        ''' + form_row('Senha', '<input type="password" placeholder="********">') + '''
        ''' + form_row('Nível', '<select><option>Admin</option><option>Moderador</option><option>Super Admin</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Criar Admin</button>
    </div></div>'''))

sections.append(section('revendedor', 'Revendedor', 'store', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-store"></i> Revendedores</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Revendedor','Créditos','Clientes','Status'],
        [['1','revenda_norte','R$ 1.250,00','28','<span class="badge-status badge-active">Ativo</span>'],
         ['2','revenda_sul','R$ 890,00','15','<span class="badge-status badge-active">Ativo</span>'],
         ['3','revenda_ne','R$ 0,00','5','<span class="badge-status badge-expired">Inativo</span>']]) + '''</div></div>
    <div class="panel"><div class="panel-header"><i class="fas fa-plus-circle"></i> Adicionar Revendedor</div><div class="panel-body">
        ''' + form_row('Nome', '<input type="text" placeholder="nome_revenda">') + '''
        ''' + form_row('Email', '<input type="email" placeholder="email@exemplo.com">') + '''
        ''' + form_row('Créditos Iniciais', '<input type="number" value="500">') + '''
        ''' + form_row('Desconto (%)', '<input type="number" value="15">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Criar Revendedor</button>
    </div></div>'''))

sections.append(section('usuarios-cs', 'Usuários CS', 'users', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-users"></i> Todos os Usuários CS</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Usuário','Protocolo','Servidor','Conexões','Validade','Status','Ações'],
        [['1','cliente01','CCCam','CCCam-01','1','15/09/2026','<span class="badge-status badge-active">Ativo</span>','<span class="copy-btn" style="padding:3px 8px;font-size:10px">Editar</span>'],
         ['2','cliente02','CCCam','CCCam-02','2','20/09/2026','<span class="badge-status badge-active">Ativo</span>','<span class="copy-btn" style="padding:3px 8px;font-size:10px">Editar</span>'],
         ['3','revenda_norte','MGcamd','MGcamd-01','5','01/12/2026','<span class="badge-status badge-active">Ativo</span>','<span class="copy-btn" style="padding:3px 8px;font-size:10px">Editar</span>'],
         ['4','teste_sp','Newcamd','Newcamd-01','1','18/08/2026','<span class="badge-status badge-test">Teste</span>','<span class="copy-btn" style="padding:3px 8px;font-size:10px">Editar</span>'],
         ['5','cliente05','CCCam','CCCam-01','1','10/08/2026','<span class="badge-status badge-expired">Expirado</span>','<span class="copy-btn" style="padding:3px 8px;font-size:10px">Editar</span>'],
         ['6','revenda_sul','OSCam','OSCam-01','10','30/11/2026','<span class="badge-status badge-active">Ativo</span>','<span class="copy-btn" style="padding:3px 8px;font-size:10px">Editar</span>']]) + '''</div></div>'''))

sections.append(section('testes', 'Testes CS', 'vial', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-vial"></i> Testes Ativos</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Usuário','Protocolo','Servidor','Criado','Expira','Status'],
        [['1','teste_sp','Newcamd','Newcamd-01','17/08/2026','18/08/2026','<span class="badge-status badge-test">Teste</span>'],
         ['2','teste_rj','CCCam','CCCam-01','16/08/2026','17/08/2026','<span class="badge-status badge-test">Teste</span>'],
         ['3','teste_mg','MGcamd','MGcamd-01','17/08/2026','20/08/2026','<span class="badge-status badge-test">Teste</span>']]) + '''</div></div>
    <div class="panel"><div class="panel-header"><i class="fas fa-plus-circle"></i> Gerar Teste CS</div><div class="panel-body">
        ''' + form_row('Protocolo', '<select><option>CCCam</option><option>MGcamd</option><option>Newcamd</option><option>OSCam</option></select>') + '''
        ''' + form_row('Servidor', '<select><option>CCCam-01</option><option>CCCam-02</option><option>MGcamd-01</option><option>Newcamd-01</option><option>OSCam-01</option></select>') + '''
        ''' + form_row('Duração', '<select><option>24 horas</option><option>48 horas</option><option>72 horas</option></select>') + '''
        ''' + form_row('Email/WhatsApp', '<input type="text" placeholder="contato do cliente">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px;background:linear-gradient(to right,#ffc107,#fd7e14)">Gerar Teste</button>
    </div></div>'''))

sections.append(section('online', 'Conexões Online', 'wifi', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-wifi"></i> Conexões Online Agora</div><div class="panel-body" style="padding:0">
        ''' + data_table(['Usuário','IP','Protocolo','Servidor','Uptime','Hops','Status'],
        [['cliente01','189.xxx.xxx.42','CCCam','CCCam-01','4h 23m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['cliente02','200.xxx.xxx.15','CCCam','CCCam-02','1h 10m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['revenda_norte','177.xxx.xxx.88','MGcamd','MGcamd-01','12h 05m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['revenda_sul','150.xxx.xxx.201','OSCam','OSCam-01','8h 47m','Hop1','<span class="badge-status badge-connected">Conectado</span>'],
         ['cliente10','100.xxx.xxx.7','Newcamd','Newcamd-01','0h 45m','Hop2','<span class="badge-status badge-connected">Conectado</span>'],
         ['cliente15','210.xxx.xxx.99','CCCam','CCCam-01','6h 12m','Hop1','<span class="badge-status badge-connected">Conectado</span>']]) + '''</div></div>
    <div style="margin-top:15px;display:flex;gap:15px">
        <div class="widget-card"><div class="widget-icon green"><i class="fas fa-wifi"></i></div><div class="widget-number">6</div><div class="widget-label">Online Agora</div></div>
        <div class="widget-card"><div class="widget-icon purple"><i class="fas fa-server"></i></div><div class="widget-number">5</div><div class="widget-label">Servidores Ativos</div></div>
    </div>'''))

# ── Linhas / Clines ──
sections.append(section('gerar-clines', 'Gerar C-Lines', 'key', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-key"></i> Gerar C-Lines</div><div class="panel-body">
        ''' + form_row('Servidor CCCam', '<select><option>CCCam-01</option><option>CCCam-02</option></select>') + '''
        ''' + form_row('Usuário', '<input type="text" placeholder="nome_usuario">') + '''
        ''' + form_row('Senha', '<input type="text" placeholder="senha_aleatoria">') + '''
        ''' + form_row('Validade (dias)', '<input type="number" value="30">') + '''
        ''' + form_row('Max. Conexões', '<input type="number" value="1">') + '''
        ''' + form_row('Hop', '<select><option>Hop1</option><option>Hop2</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Gerar C-Line</button>
    </div></div>'''))

sections.append(section('minhas-linhas', 'Minhas Linhas', 'file-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-file-alt"></i> Todas as Minhas Linhas</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Tipo','Linha','Validade','Status'],
        [['1','<span class="proto-tag proto-cccam">CCCam</span>','C: cs1.homerfull.net 12000 user1 pass1','15/09/2026','<span class="badge-status badge-active">Ativo</span>'],
         ['2','<span class="proto-tag proto-mgcamd">MGcamd</span>','MG: cs1.homerfull.net 15000 user2 pass2','01/12/2026','<span class="badge-status badge-active">Ativo</span>'],
         ['3','<span class="proto-tag proto-newcamd">Newcamd</span>','N: cs1.homerfull.net 16000 user3 pass3 01...14','18/08/2026','<span class="badge-status badge-test">Teste</span>'],
         ['4','<span class="proto-tag proto-cccam">CCCam</span>','C: cs2.homerfull.net 12000 user4 pass4','10/08/2026','<span class="badge-status badge-expired">Expirado</span>']]) + '''</div></div>'''))

sections.append(section('linhas-expiradas', 'Linhas Expiradas', 'clock', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-clock"></i> Linhas Expiradas</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Usuário','Tipo','Linha','Expirou','Ações'],
        [['1','cliente05','CCCam','C: cs1.homerfull.net 12000 cliente05 pass5','10/08/2026','<span class="copy-btn" style="padding:3px 8px;font-size:10px;background:#28a745">Renovar</span>'],
         ['2','cliente_ant','MGcamd','MG: cs1.homerfull.net 15000 cliente_ant pass6','01/07/2026','<span class="copy-btn" style="padding:3px 8px;font-size:10px;background:#28a745">Renovar</span>'],
         ['3','velho_user','Newcamd','N: cs1.homerfull.net 16000 velho_user pass7','15/06/2026','<span class="copy-btn" style="padding:3px 8px;font-size:10px;background:#dc3545">Deletar</span>']]) + '''</div></div>'''))

sections.append(section('linhas-bloqueadas', 'Linhas Bloqueadas', 'ban', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-ban"></i> Linhas Bloqueadas</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Usuário','Tipo','Motivo','Data','Ações'],
        [['1','fraud_user','CCCam','Compartilhamento ilegal detectado','12/08/2026','<span class="copy-btn" style="padding:3px 8px;font-size:10px;background:#28a745">Desbloquear</span>'],
         ['2','spam_bot','CCCam','Múltiplas conexões simultâneas','05/08/2026','<span class="copy-btn" style="padding:3px 8px;font-size:10px;background:#dc3545">Deletar</span>']]) + '''</div></div>'''))

# ── Pagamentos ──
sections.append(section('comprar-creditos', 'Comprar Créditos', 'shopping-cart', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-shopping-cart"></i> Comprar Créditos CS</div><div class="panel-body">
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-bottom:20px">
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:2px solid #e2d8ff"><div style="font-size:24px;font-weight:700;color:#6967CE;font-family:Comfortaa">R$ 50</div><div style="font-size:12px;color:#75798f;margin:5px 0">50 Créditos</div><button class="copy-btn">Comprar</button></div>
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:2px solid #6967CE"><div style="font-size:24px;font-weight:700;color:#6967CE;font-family:Comfortaa">R$ 180</div><div style="font-size:12px;color:#75798f;margin:5px 0">200 Créditos</div><div style="font-size:10px;color:#28a745;font-weight:700">10% OFF</div><button class="copy-btn" style="background:#28a745">Comprar</button></div>
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:2px solid #e2d8ff"><div style="font-size:24px;font-weight:700;color:#6967CE;font-family:Comfortaa">R$ 400</div><div style="font-size:12px;color:#75798f;margin:5px 0">500 Créditos</div><div style="font-size:10px;color:#28a745;font-weight:700">20% OFF</div><button class="copy-btn">Comprar</button></div>
        </div>
    </div></div>'''))

sections.append(section('minhas-compras', 'Minhas Compras', 'receipt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-receipt"></i> Histórico de Compras</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Data','Plano','Valor','Pagamento','Status'],
        [['1','15/08/2026','200 Créditos','R$ 180,00','PagSeguro','<span class="badge-status badge-active">Aprovado</span>'],
         ['2','01/08/2026','50 Créditos','R$ 50,00','PayPal','<span class="badge-status badge-active">Aprovado</span>'],
         ['3','15/07/2026','500 Créditos','R$ 400,00','MercadoPago','<span class="badge-status badge-active">Aprovado</span>']]) + '''</div></div>'''))

sections.append(section('minhas-vendas', 'Minhas Vendas', 'exchange-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-exchange-alt"></i> Vendas Realizadas</div><div class="panel-body" style="padding:0">
        ''' + data_table(['#','Cliente','Plano','Valor','Data','Status'],
        [['1','cliente01','30 dias CCCam','R$ 25,00','16/08/2026','<span class="badge-status badge-active">Pago</span>'],
         ['2','cliente02','90 dias CCCam','R$ 60,00','15/08/2026','<span class="badge-status badge-active">Pago</span>'],
         ['3','revenda_norte','Revenda 30 dias','R$ 150,00','10/08/2026','<span class="badge-status badge-active">Pago</span>']]) + '''</div></div>'''))

sections.append(section('criar-plano', 'Criar Plano CS', 'credit-card', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-credit-card"></i> Criar Plano de Serviço CS</div><div class="panel-body">
        ''' + form_row('Nome do Plano', '<input type="text" placeholder="Ex: Plano Mensal CCCam">') + '''
        ''' + form_row('Protocolo', '<select><option>CCCam</option><option>MGcamd</option><option>Newcamd</option><option>OSCam</option></select>') + '''
        ''' + form_row('Duração (dias)', '<input type="number" value="30">') + '''
        ''' + form_row('Max. Conexões', '<input type="number" value="1">') + '''
        ''' + form_row('Preço (R$)', '<input type="text" placeholder="25.00">') + '''
        ''' + form_row('Créditos Necessários', '<input type="number" value="25">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Criar Plano</button>
    </div></div>'''))

sections.append(section('pagseguro', 'PagSeguro', 'money-check-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-money-check-alt"></i> Configuração PagSeguro</div><div class="panel-body">
        ''' + form_row('Email PagSeguro', '<input type="email" placeholder="seuemail@pagseguro.com">') + '''
        ''' + form_row('Token de Produção', '<input type="text" placeholder="********">') + '''
        ''' + form_row('Sandbox', '<select><option>Não</option><option>Sim</option></select>') + '''
        ''' + form_row('Notificação URL', '<input type="text" value="https://homerfull.com/pagseguro/notification">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Config</button>
    </div></div>'''))

sections.append(section('paypal', 'PayPal', 'paypal', '''
    <div class="panel"><div class="panel-header"><i class="fab fa-paypal"></i> Configuração PayPal</div><div class="panel-body">
        ''' + form_row('Client ID', '<input type="text" placeholder="AXXXXXXXXXX">') + '''
        ''' + form_row('Secret', '<input type="password" placeholder="********">') + '''
        ''' + form_row('Modo', '<select><option>Live</option><option>Sandbox</option></select>') + '''
        ''' + form_row('Currency', '<select><option>BRL</option><option>USD</option><option>EUR</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Config PayPal</button>
    </div></div>'''))

sections.append(section('mercadopago', 'MercadoPago', 'money-check-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-money-check-alt"></i> Configuração MercadoPago</div><div class="panel-body">
        ''' + form_row('Access Token', '<input type="text" placeholder="APP_XXXXX">') + '''
        ''' + form_row('Public Key', '<input type="text" placeholder="APP_YYYYY">') + '''
        ''' + form_row('Modo', '<select><option>Produção</option><option>Sandbox</option></select>') + '''
        ''' + form_row('Webhook URL', '<input type="text" value="https://homerfull.com/mercadopago/webhook">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Config MercadoPago</button>
    </div></div>'''))

# ── Redes Sociais ──
sections.append(section('whatsapp', 'WhatsApp', 'whatsapp', '''
    <div class="panel"><div class="panel-header"><i class="fab fa-whatsapp"></i> Configuração WhatsApp</div><div class="panel-body">
        ''' + form_row('Número WhatsApp', '<input type="text" placeholder="+55 11 99999-9999">') + '''
        ''' + form_row('API URL', '<input type="text" value="https://api.whatsapp.com/send?phone="><br>') + '''
        ''' + form_row('Mensagem Padrão', '<textarea rows="3" style="width:100%;padding:10px;border:1px solid #e2d8ff;border-radius:8px;font-family:Muli;font-size:13px" placeholder="Olá! Bem-vindo ao HomerFull CS...">Olá! Bem-vindo ao HomerFull CS Panel. Aqui estão suas linhas:</textarea>') + '''
        ''' + form_row('Envio Automático', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px;background:#25D366">Salvar WhatsApp</button>
    </div></div>'''))

sections.append(section('telegram', 'Telegram', 'telegram', '''
    <div class="panel"><div class="panel-header"><i class="fab fa-telegram"></i> Configuração Telegram Bot</div><div class="panel-body">
        ''' + form_row('Bot Token', '<input type="text" placeholder="123456:ABC-DEF...">') + '''
        ''' + form_row('Chat ID', '<input type="text" placeholder="-100123456789">') + '''
        ''' + form_row('Mensagem Padrão', '<textarea rows="3" style="width:100%;padding:10px;border:1px solid #e2d8ff;border-radius:8px;font-family:Muli;font-size:13px">Suas linhas CS estão prontas!</textarea>') + '''
        ''' + form_row('Envio Automático', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px;background:#0088cc">Salvar Telegram</button>
    </div></div>'''))

# ── Relatório ──
sections.append(section('relatorios', 'Relatórios', 'chart-bar', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-chart-bar"></i> Relatórios CS</div><div class="panel-body">
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:15px;margin-bottom:20px">
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:1px solid #e2d8ff;cursor:pointer" onclick="alert('Relatório de Vendas gerado!')"><i class="fas fa-chart-line" style="font-size:30px;color:#6967CE"></i><div style="margin-top:10px;font-weight:700;color:#404666">Relatório de Vendas</div><div style="font-size:11px;color:#75798f">Vendas por período</div></div>
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:1px solid #e2d8ff;cursor:pointer" onclick="alert('Relatório de Usuários gerado!')"><i class="fas fa-users" style="font-size:30px;color:#28a745"></i><div style="margin-top:10px;font-weight:700;color:#404666">Relatório de Usuários</div><div style="font-size:11px;color:#75798f">Usuários ativos/expirados</div></div>
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:1px solid #e2d8ff;cursor:pointer" onclick="alert('Relatório de Servidores gerado!')"><i class="fas fa-server" style="font-size:30px;color:#ffc107"></i><div style="margin-top:10px;font-weight:700;color:#404666">Relatório de Servidores</div><div style="font-size:11px;color:#75798f">Uptime e performance</div></div>
            <div style="background:#f7f5ff;padding:20px;border-radius:10px;text-align:center;border:1px solid #e2d8ff;cursor:pointer" onclick="alert('Relatório Financeiro gerado!')"><i class="fas fa-coins" style="font-size:30px;color:#dc3545"></i><div style="margin-top:10px;font-weight:700;color:#404666">Relatório Financeiro</div><div style="font-size:11px;color:#75798f">Receitas e despesas</div></div>
        </div>
    </div></div>'''))

sections.append(section('estatisticas', 'Estatísticas', 'chart-line', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-chart-line"></i> Estatísticas do Sistema</div><div class="panel-body">
        <div class="widgets-row">
            <div class="widget-card"><div class="widget-icon purple"><i class="fas fa-users"></i></div><div class="widget-number">127</div><div class="widget-label">Total Usuários</div></div>
            <div class="widget-card"><div class="widget-icon green"><i class="fas fa-check-circle"></i></div><div class="widget-number">112</div><div class="widget-label">Ativos</div></div>
            <div class="widget-card"><div class="widget-icon orange"><i class="fas fa-clock"></i></div><div class="widget-number">10</div><div class="widget-label">Testes</div></div>
            <div class="widget-card"><div class="widget-icon red"><i class="fas fa-times-circle"></i></div><div class="widget-number">5</div><div class="widget-label">Expirados</div></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:10px">
            <div style="background:#f7f5ff;padding:18px;border-radius:10px"><div style="font-size:12px;color:#75798f;font-weight:700;margin-bottom:8px">DISTRIBUIÇÃO POR PROTOCOLO</div>
                <div style="margin-bottom:6px"><span style="font-size:12px;color:#404666">CCCam: </span><span style="font-weight:700;color:#6967CE">58%</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill purple" style="width:58%"></div></div></div>
                <div style="margin-bottom:6px"><span style="font-size:12px;color:#404666">MGcamd: </span><span style="font-weight:700;color:#28a745">22%</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill green" style="width:22%"></div></div></div>
                <div style="margin-bottom:6px"><span style="font-size:12px;color:#404666">Newcamd: </span><span style="font-weight:700;color:#004085">12%</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill" style="width:12%;background:#004085"></div></div></div>
                <div><span style="font-size:12px;color:#404666">OSCam: </span><span style="font-weight:700;color:#856404">8%</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill orange" style="width:8%"></div></div></div>
            </div>
            <div style="background:#f7f5ff;padding:18px;border-radius:10px"><div style="font-size:12px;color:#75798f;font-weight:700;margin-bottom:8px">RECEITA MENSAL</div>
                <div style="font-size:28px;font-weight:700;color:#404666;font-family:Comfortaa">R$ 4.250</div>
                <div style="font-size:11px;color:#28a745;margin-top:5px">↑ 12% vs mês anterior</div>
                <div style="margin-top:10px"><div style="margin-bottom:6px"><span style="font-size:12px">PagSeguro: R$ 2.100</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill purple" style="width:49%"></div></div></div>
                <div style="margin-bottom:6px"><span style="font-size:12px">PayPal: R$ 950</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill" style="width:22%;background:#0088cc"></div></div></div>
                <div><span style="font-size:12px">MercadoPago: R$ 1.200</span><div class="progress-bar" style="margin-top:4px"><div class="progress-fill orange" style="width:28%"></div></div></div></div>
            </div>
        </div>
    </div></div>'''))

# ── Configurações ──
sections.append(section('config-servidor', 'Configuração do Servidor', 'cogs', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-cogs"></i> Configuração Geral do Servidor</div><div class="panel-body">
        ''' + form_row('Nome do Servidor', '<input type="text" value="HomerFull CS Panel">') + '''
        ''' + form_row('URL do Painel', '<input type="text" value="https://homerfull.com">') + '''
        ''' + form_row('IP Principal', '<input type="text" value="192.168.1.100">') + '''
        ''' + form_row('Timezone', '<select><option>America/Sao_Paulo</option><option>America/Manaus</option><option>America/Belem</option></select>') + '''
        ''' + form_row('Modo Manutenção', '<select><option>Desativado</option><option>Ativado</option></select>') + '''
        ''' + form_row('Logo URL', '<input type="text" value="/assets/img/logo.png">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Config</button>
    </div></div>'''))

sections.append(section('email', 'Configuração Email', 'envelope', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-envelope"></i> Configuração de Email SMTP</div><div class="panel-body">
        ''' + form_row('SMTP Host', '<input type="text" value="smtp.gmail.com">') + '''
        ''' + form_row('SMTP Porta', '<input type="number" value="587">') + '''
        ''' + form_row('Email', '<input type="email" placeholder="seuemail@gmail.com">') + '''
        ''' + form_row('Senha', '<input type="password" placeholder="********">') + '''
        ''' + form_row('Segurança', '<select><option>TLS</option><option>SSL</option><option>Nenhuma</option></select>') + '''
        ''' + form_row('Email De', '<input type="text" value="noreply@homerfull.com">') + '''
        ''' + form_row('Nome De', '<input type="text" value="HomerFull CS">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Email</button>
    </div></div>'''))

sections.append(section('sms', 'Configuração SMS', 'sms', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-sms"></i> Configuração SMS</div><div class="panel-body">
        ''' + form_row('Provider', '<select><option>Twilio</option><option>Vonage</option><option>Zenvia</option></select>') + '''
        ''' + form_row('API Key', '<input type="text" placeholder="SUA_API_KEY">') + '''
        ''' + form_row('API Secret', '<input type="password" placeholder="********">') + '''
        ''' + form_row('Número Origem', '<input type="text" placeholder="+5511999999999">') + '''
        ''' + form_row('Envio Automático', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar SMS</button>
    </div></div>'''))

sections.append(section('seguranca', 'Segurança', 'shield-alt', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-shield-alt"></i> Configuração de Segurança</div><div class="panel-body">
        ''' + form_row('Tentativas Login Máx.', '<input type="number" value="5">') + '''
        ''' + form_row('Bloqueio IP (min)', '<input type="number" value="30">') + '''
        ''' + form_row('2FA Admin', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        ''' + form_row('HTTPS Forçado', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        ''' + form_row('Max Conexões/IP', '<input type="number" value="3">') + '''
        ''' + form_row('Anti-Sharing Detection', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        ''' + form_row('Log de Acessos', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Segurança</button>
    </div></div>'''))

# ── Opções ──
sections.append(section('opcoes', 'Opções do Sistema', 'sliders-h', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-sliders-h"></i> Opções Gerais</div><div class="panel-body">
        ''' + form_row('Idioma', '<select><option>Português (BR)</option><option>Español</option><option>English</option></select>') + '''
        ''' + form_row('Tema', '<select><option>Claro</option><option>Escuro</option><option>Automático</option></select>') + '''
        ''' + form_row('Notificações Push', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        ''' + form_row('Som de Alerta', '<select><option>Ativado</option><option>Desativado</option></select>') + '''
        ''' + form_row('Auto-Logout (min)', '<input type="number" value="30">') + '''
        ''' + form_row('Mostrar Hops', '<select><option>Sim</option><option>Não</option></select>') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Opções</button>
    </div></div>'''))

# ── Suporte ──
sections.append(section('suporte', 'Suporte', 'headset', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-headset"></i> Central de Suporte</div><div class="panel-body">
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:15px;margin-bottom:20px">
            <div style="background:#f7f5ff;padding:25px;border-radius:10px;text-align:center;border:1px solid #e2d8ff"><i class="fab fa-whatsapp" style="font-size:40px;color:#25D366"></i><div style="margin-top:10px;font-weight:700;color:#404666">WhatsApp</div><div style="font-size:12px;color:#75798f">+55 11 99999-0000</div></div>
            <div style="background:#f7f5ff;padding:25px;border-radius:10px;text-align:center;border:1px solid #e2d8ff"><i class="fab fa-telegram" style="font-size:40px;color:#0088cc"></i><div style="margin-top:10px;font-weight:700;color:#404666">Telegram</div><div style="font-size:12px;color:#75798f">@HomerFullSuporte</div></div>
            <div style="background:#f7f5ff;padding:25px;border-radius:10px;text-align:center;border:1px solid #e2d8ff"><i class="fas fa-envelope" style="font-size:40px;color:#6967CE"></i><div style="margin-top:10px;font-weight:700;color:#404666">Email</div><div style="font-size:12px;color:#75798f">suporte@homerfull.com</div></div>
            <div style="background:#f7f5ff;padding:25px;border-radius:10px;text-align:center;border:1px solid #e2d8ff"><i class="fas fa-book" style="font-size:40px;color:#ffc107"></i><div style="margin-top:10px;font-weight:700;color:#404666">Wiki / FAQ</div><div style="font-size:12px;color:#75798f">docs.homerfull.com</div></div>
        </div>
    </div></div>'''))

# ── Template ──
sections.append(section('template', 'Template', 'palette', '''
    <div class="panel"><div class="panel-header"><i class="fas fa-palette"></i> Personalização de Template</div><div class="panel-body">
        ''' + form_row('Cor Primária', '<input type="color" value="#6967CE" style="width:80px;height:40px;border:1px solid #e2d8ff;border-radius:8px;cursor:pointer">') + '''
        ''' + form_row('Cor Secundária', '<input type="color" value="#32cafe" style="width:80px;height:40px;border:1px solid #e2d8ff;border-radius:8px;cursor:pointer">') + '''
        ''' + form_row('Logo do Painel', '<input type="file" accept="image/*">') + '''
        ''' + form_row('Background Login', '<input type="file" accept="image/*">') + '''
        ''' + form_row('Favicon', '<input type="file" accept="image/*">') + '''
        ''' + form_row('Título do Painel', '<input type="text" value="HomerFull CS Panel">') + '''
        ''' + form_row('Footer Text', '<input type="text" value="HomerFull CS Panel v3.0 © 2026">') + '''
        <button class="login-btn" style="max-width:300px;margin-top:10px">Salvar Template</button>
    </div></div>'''))


# ═══════ BUILD HTML ═══════
all_sections = '\n'.join(sections)

html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HomerFull CS Panel - Preview</title>
<link rel="icon" href="data:image/x-icon;base64,{ico_b64}">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;400;500;600;700&family=Muli:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Muli',sans-serif; font-size:14px; color:#404666; background:#eff0f5; }}
h1,h2,h3,h4,h5,h6 {{ font-family:'Comfortaa',cursive; }}
a {{ text-decoration:none; color:inherit; }}
button {{ cursor:pointer; border:none; outline:none; }}

.view-toggle {{
    position:fixed; top:15px; right:20px; z-index:10000;
    display:flex; gap:8px;
}}
.view-toggle button {{
    padding:8px 18px; border-radius:20px; font-size:13px; font-weight:600;
    font-family:'Muli',sans-serif; transition:all .3s;
    box-shadow:0 2px 8px rgba(0,0,0,0.15);
}}
.view-toggle .btn-login {{
    background:linear-gradient(to right,#995193,#ba426d,#9a5192); color:#fff;
}}
.view-toggle .btn-dashboard {{
    background:linear-gradient(to right,#9f78ff,#32cafe); color:#fff;
}}
.view-toggle button.active {{ transform:scale(1.05); box-shadow:0 4px 15px rgba(0,0,0,0.25); }}

/* ===== LOGIN ===== */
#login-view {{
    min-height:100vh; display:flex; align-items:center; justify-content:center;
    background:url('data:image/jpeg;base64,{bg_b64}') center/cover no-repeat;
    position:relative;
}}
#login-view::before {{
    content:''; position:absolute; inset:0;
    background:rgba(0,0,0,0.4);
}}
.login-container {{
    position:relative; z-index:2; width:100%; max-width:450px; padding:20px;
    animation:fadeInDown .8s ease;
}}
@keyframes fadeInDown {{
    0% {{ opacity:0; transform:translateY(-30px); }}
    100% {{ opacity:1; transform:translateY(0); }}
}}
.login-box {{
    background:#fff; border-radius:12px; padding:40px 35px;
    box-shadow:0 10px 40px rgba(0,0,0,0.3);
}}
.login-logo {{ text-align:center; margin-bottom:25px; }}
.login-logo img {{ max-width:200px; height:auto; }}
.login-title {{
    text-align:center; font-family:'Comfortaa',cursive; font-size:20px;
    color:#6967CE; margin-bottom:8px; font-weight:700;
}}
.login-subtitle {{
    text-align:center; font-size:12px; color:#75798f; margin-bottom:25px;
    letter-spacing:1px;
}}
.login-form-group {{ margin-bottom:18px; }}
.login-form-group label {{
    display:block; margin-bottom:6px; font-size:13px; color:#75798f; font-weight:500;
}}
.login-form-group input {{
    width:100%; padding:12px 15px; border:1px solid #e2d8ff; border-radius:8px;
    background:#fcfbff; font-size:14px; color:#404666; font-family:'Muli',sans-serif;
    transition:border-color .3s;
}}
.login-form-group input:focus {{
    border-color:#6967CE; outline:none; box-shadow:0 0 0 3px rgba(105,103,206,0.1);
}}
.login-btn {{
    width:100%; padding:13px; border-radius:8px; font-size:15px; font-weight:600;
    font-family:'Muli',sans-serif; color:#fff; margin-top:5px;
    background:linear-gradient(to right,#995193 0%,#ba426d 51%,#9a5192 100%);
    background-size:200% auto; transition:background-position .4s;
}}
.login-btn:hover {{ background-position:right center; }}
.login-footer {{
    text-align:center; margin-top:20px; font-size:12px; color:#75798f;
}}
.login-footer a {{ color:#6967CE; }}
.login-remember {{
    display:flex; align-items:center; gap:8px; margin-bottom:15px;
}}
.login-remember input[type=checkbox] {{ accent-color:#6967CE; }}

/* ===== DASHBOARD ===== */
#dashboard-view {{ display:none; min-height:100vh; }}

/* Top Bar */
.topbar {{
    position:fixed; top:0; left:250px; right:0; height:60px; z-index:100;
    background:linear-gradient(to right,#9f78ff,#32cafe);
    display:flex; align-items:center; justify-content:space-between;
    padding:0 25px; color:#fff;
}}
.topbar-left {{ display:flex; align-items:center; gap:20px; }}
.topbar-left i {{ font-size:18px; cursor:pointer; }}
.topbar-right {{ display:flex; align-items:center; gap:15px; }}
.topbar-right .notif {{ position:relative; cursor:pointer; }}
.topbar-right .notif .badge {{
    position:absolute; top:-5px; right:-8px; background:#ba426d; color:#fff;
    font-size:9px; padding:2px 5px; border-radius:10px;
}}
.topbar-right .user-info {{
    display:flex; align-items:center; gap:8px; cursor:pointer;
}}
.topbar-right .user-avatar {{
    width:35px; height:35px; border-radius:50%;
    background:#fff; display:flex; align-items:center; justify-content:center;
    color:#6967CE; font-weight:700; font-size:14px;
}}
.topbar-page-title {{
    font-family:'Comfortaa',cursive; font-size:16px; font-weight:600;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
}}

/* Sidebar */
.sidebar {{
    position:fixed; top:0; left:0; width:250px; height:100vh; z-index:200;
    background:#fff; border-right:1px solid #e8e8e8;
    overflow-y:auto; overflow-x:hidden;
    transition:transform .3s, width .3s;
}}
.sidebar-logo {{
    padding:18px 20px; text-align:center; border-bottom:1px solid #f0f0f0;
}}
.sidebar-logo img {{ max-width:80px; height:auto; }}
.sidebar-menu {{ padding:10px 0; }}
.sidebar-menu .menu-header {{
    padding:12px 20px 5px; font-size:10px; text-transform:uppercase;
    letter-spacing:1.2px; color:#998fbf; font-weight:700;
    font-family:'Comfortaa',cursive;
}}
.sidebar-menu .menu-item {{
    display:flex; align-items:center; gap:12px; padding:10px 20px;
    color:#555; font-size:13px; font-weight:500; cursor:pointer;
    transition:all .2s; border-left:3px solid transparent;
}}
.sidebar-menu .menu-item:hover {{
    background:#f7f5ff; color:#6967CE; border-left-color:#6967CE;
}}
.sidebar-menu .menu-item.active {{
    background:linear-gradient(to right,#f7f5ff,#eff0f5); color:#6967CE;
    border-left-color:#6967CE; font-weight:600;
}}
.sidebar-menu .menu-item i {{ width:20px; text-align:center; font-size:14px; }}
.sidebar-menu .menu-item .submenu-arrow {{
    margin-left:auto; font-size:10px; transition:transform .3s;
}}
.sidebar-menu .menu-item.open .submenu-arrow {{ transform:rotate(90deg); }}
.sidebar-menu .submenu {{ display:none; background:#fbfaff; }}
.sidebar-menu .submenu.show {{ display:block; }}
.sidebar-menu .submenu .menu-item {{ padding-left:52px; font-size:12px; }}
.sidebar-pro-badge {{
    margin:15px 20px; padding:12px 15px; border-radius:10px;
    background:linear-gradient(135deg,#9f78ff,#32cafe);
    text-align:center; color:#fff; font-size:11px; font-weight:600;
}}
.sidebar-pro-badge img {{ width:40px; margin-bottom:5px; }}
.sidebar-version {{
    padding:10px 20px; font-size:10px; color:#aaa; text-align:center;
    border-top:1px solid #f0f0f0; margin-top:10px;
}}

/* Main Content */
.main-content {{ margin-left:250px; margin-top:60px; padding:25px; }}

/* Section Pages */
.section-title {{
    font-family:'Comfortaa',cursive; font-size:20px; font-weight:700;
    color:#6967CE; margin-bottom:20px; display:flex; align-items:center; gap:10px;
}}
.section-title i {{ font-size:22px; }}
.section-page {{ animation:fadeIn .3s ease; }}
@keyframes fadeIn {{
    0% {{ opacity:0; transform:translateY(10px); }}
    100% {{ opacity:1; transform:translateY(0); }}
}}

/* Form rows */
.form-row {{
    display:grid; grid-template-columns:180px 1fr; gap:10px; align-items:center;
    margin-bottom:14px;
}}
.form-row label {{
    font-size:13px; color:#75798f; font-weight:600; text-align:right;
}}
.form-row input, .form-row select, .form-row textarea {{
    padding:10px 14px; border:1px solid #e2d8ff; border-radius:8px;
    background:#fcfbff; font-size:13px; color:#404666; font-family:'Muli',sans-serif;
    transition:border-color .3s;
}}
.form-row input:focus, .form-row select:focus, .form-row textarea:focus {{
    border-color:#6967CE; outline:none; box-shadow:0 0 0 3px rgba(105,103,206,0.1);
}}

/* Widgets */
.widgets-row {{
    display:grid; grid-template-columns:repeat(4,1fr); gap:20px; margin-bottom:25px;
}}
.widget-card {{
    background:#fff; border-radius:10px; padding:20px; text-align:center;
    box-shadow:0 2px 10px rgba(0,0,0,0.06);
    border:1px solid #f0f0f0; transition:transform .2s;
}}
.widget-card:hover {{ transform:translateY(-3px); box-shadow:0 5px 20px rgba(0,0,0,0.1); }}
.widget-icon {{
    width:55px; height:55px; border-radius:50%; margin:0 auto 12px;
    display:flex; align-items:center; justify-content:center;
}}
.widget-icon i {{ font-size:22px; }}
.widget-icon.purple {{ background:rgba(105,103,206,0.1); }}
.widget-icon.purple i {{ color:#6967CE; }}
.widget-icon.green {{ background:rgba(40,167,69,0.1); }}
.widget-icon.green i {{ color:#28a745; }}
.widget-icon.red {{ background:rgba(220,53,69,0.1); }}
.widget-icon.red i {{ color:#dc3545; }}
.widget-icon.orange {{ background:rgba(255,193,7,0.1); }}
.widget-icon.orange i {{ color:#ffc107; }}
.widget-number {{ font-size:28px; font-weight:700; color:#404666; font-family:'Comfortaa'; }}
.widget-label {{ font-size:12px; color:#75798f; margin-top:4px; font-weight:500; text-transform:uppercase; letter-spacing:.5px; }}

/* Panels */
.panel {{
    background:#fff; border-radius:10px; margin-bottom:20px;
    box-shadow:0 2px 10px rgba(0,0,0,0.05); border:1px solid #f0f0f0;
    overflow:hidden;
}}
.panel-header {{
    padding:15px 20px; font-family:'Comfortaa',cursive; font-size:14px;
    font-weight:600; color:#fff; display:flex; align-items:center; gap:10px;
    background:linear-gradient(to right,#9f78ff,#32cafe);
}}
.panel-body {{ padding:20px; }}
.panel-footer {{
    padding:12px 20px; text-align:center; font-size:11px; color:#aaa;
    border-top:1px solid #f0f0f0;
}}

/* Server Status */
.server-status-grid {{
    display:grid; grid-template-columns:repeat(3,1fr); gap:15px;
}}
.server-box {{
    background:#f7f5ff; padding:18px; border-radius:10px; text-align:center;
    border:1px solid #e2d8ff; transition:all .2s;
}}
.server-box:hover {{ border-color:#6967CE; }}
.server-box .status-dot {{
    width:12px; height:12px; border-radius:50%; display:inline-block; margin-bottom:8px;
}}
.server-box .status-dot.online {{ background:#28a745; box-shadow:0 0 8px rgba(40,167,69,0.5); }}
.server-box .status-dot.offline {{ background:#dc3545; box-shadow:0 0 8px rgba(220,53,69,0.5); }}
.server-box .sv-name {{ font-size:16px; font-weight:700; color:#404666; font-family:'Comfortaa'; margin-bottom:4px; }}
.server-box .sv-info {{ font-size:11px; color:#75798f; }}
.server-box .sv-badge {{
    display:inline-block; padding:3px 10px; border-radius:12px; font-size:10px;
    font-weight:700; text-transform:uppercase; margin-top:8px;
}}
.sv-badge.online {{ background:#d4edda; color:#155724; }}
.sv-badge.offline {{ background:#f8d7da; color:#721c24; }}

/* C-Line Boxes */
.cline-box {{
    display:flex; align-items:center; gap:10px; padding:12px 15px;
    background:#fbfaff; border:1px solid #e2d8ff; border-radius:8px;
    margin-bottom:10px; font-family:'Courier New',monospace;
}}
.cline-box .cline-label {{
    font-size:11px; color:#75798f; min-width:60px; font-weight:700;
    text-transform:uppercase; font-family:'Muli',sans-serif;
}}
.cline-box .cline-value {{
    flex:1; font-size:12px; color:#6967CE; word-break:break-all;
}}
.cline-box .copy-btn {{
    padding:5px 12px; border-radius:5px; font-size:11px; font-weight:600;
    background:#6967CE; color:#fff; cursor:pointer; transition:background .2s;
    font-family:'Muli',sans-serif;
}}
.cline-box .copy-btn:hover {{ background:#5a58b8; }}

/* Data Tables */
.data-table {{ width:100%; border-collapse:collapse; }}
.data-table th {{
    background:#f7f5ff; padding:12px 15px; text-align:left;
    font-size:11px; color:#75798f; font-weight:700; text-transform:uppercase;
    letter-spacing:.5px; border-bottom:2px solid #e2d8ff;
}}
.data-table td {{
    padding:10px 15px; font-size:13px; color:#404666; border-bottom:1px solid #f0f0f0;
}}
.data-table tr:hover td {{ background:#fbfaff; }}
.badge-status {{
    padding:3px 10px; border-radius:12px; font-size:10px; font-weight:700;
    text-transform:uppercase; letter-spacing:.5px;
}}
.badge-active {{ background:#d4edda; color:#155724; }}
.badge-expired {{ background:#f8d7da; color:#721c24; }}
.badge-test {{ background:#fff3cd; color:#856404; }}
.badge-connected {{ background:#cce5ff; color:#004085; }}

/* Info Grid */
.info-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }}

/* Progress Bars */
.progress-bar {{
    height:8px; background:#e8e8e8; border-radius:4px; overflow:hidden; margin-top:6px;
}}
.progress-fill {{ height:100%; border-radius:4px; transition:width .6s; }}
.progress-fill.green {{ background:linear-gradient(to right,#28a745,#20c997); }}
.progress-fill.orange {{ background:linear-gradient(to right,#ffc107,#fd7e14); }}
.progress-fill.red {{ background:linear-gradient(to right,#dc3545,#c82333); }}
.progress-fill.purple {{ background:linear-gradient(to right,#6967CE,#9f78ff); }}

/* Protocol Tag */
.proto-tag {{
    display:inline-flex; align-items:center; gap:5px; padding:4px 10px;
    border-radius:6px; font-size:10px; font-weight:700;
}}
.proto-cccam {{ background:#e8daef; color:#6967CE; }}
.proto-mgcamd {{ background:#d4edda; color:#155724; }}
.proto-newcamd {{ background:#cce5ff; color:#004085; }}
.proto-occam {{ background:#fff3cd; color:#856404; }}

@media(max-width:992px) {{
    .widgets-row {{ grid-template-columns:repeat(2,1fr); }}
    .info-grid {{ grid-template-columns:1fr; }}
    .server-status-grid {{ grid-template-columns:1fr 1fr; }}
    .form-row {{ grid-template-columns:1fr; }}
    .form-row label {{ text-align:left; }}
}}
@media(max-width:768px) {{
    .sidebar {{ transform:translateX(-100%); }}
    .topbar {{ left:0; }}
    .main-content {{ margin-left:0; }}
    .widgets-row {{ grid-template-columns:1fr 1fr; }}
    .server-status-grid {{ grid-template-columns:1fr; }}
}}
</style>
</head>
<body>

<div class="view-toggle">
    <button class="btn-login active" onclick="showView('login')">&#x1F510; Login</button>
    <button class="btn-dashboard" onclick="showView('dashboard')">&#x1F4CA; Painel CS</button>
</div>

<!-- ===== LOGIN ===== -->
<div id="login-view">
    <div class="login-container">
        <div class="login-box">
            <div class="login-logo">
                <img src="data:image/png;base64,{logo_b64}" alt="HomerFull CS">
            </div>
            <div class="login-title">Painel CS Card Sharing</div>
            <div class="login-subtitle">GERENCIAMENTO DE SERVIDORES CCS / MG / NC</div>
            <div class="login-form-group">
                <label><i class="fas fa-user" style="margin-right:5px;color:#6967CE"></i> Usuário</label>
                <input type="text" placeholder="Digite seu usuário" value="admin">
            </div>
            <div class="login-form-group">
                <label><i class="fas fa-lock" style="margin-right:5px;color:#6967CE"></i> Senha</label>
                <input type="password" placeholder="Digite sua senha" value="******">
            </div>
            <div class="login-remember">
                <input type="checkbox" id="remember" checked>
                <label for="remember" style="font-size:12px;color:#75798f">Lembrar meus dados</label>
            </div>
            <button class="login-btn" onclick="showView('dashboard')">Acessar Painel</button>
            <div class="login-footer">
                <a href="#">Esqueceu sua senha?</a> &middot; HomerFull CS Panel v3.0
            </div>
        </div>
    </div>
</div>

<!-- ===== DASHBOARD ===== -->
<div id="dashboard-view">
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="sidebar-logo">
            <img src="data:image/png;base64,{logo_b64}" alt="HomerFull CS">
        </div>
        <div class="sidebar-menu">
            <div class="menu-item active" onclick="navigateTo('inicio','Início',this)"><i class="fas fa-home"></i> Início</div>

            <div class="menu-header">Servidores CS</div>
            <div class="menu-item" onclick="toggleSub(this)">
                <i class="fas fa-server"></i> CCCam <i class="fas fa-chevron-right submenu-arrow"></i>
            </div>
            <div class="submenu">
                <div class="menu-item" onclick="navigateTo('cccam-add','Adicionar Servidor CCCam',this)"><i class="fas fa-plus-circle"></i> Adicionar Servidor</div>
                <div class="menu-item" onclick="navigateTo('cccam-list','Listar Servidores CCCam',this)"><i class="fas fa-list"></i> Listar Servidores</div>
                <div class="menu-item" onclick="navigateTo('cccam-clines','Gerar C-Lines CCCam',this)"><i class="fas fa-key"></i> Gerar C-Lines</div>
                <div class="menu-item" onclick="navigateTo('cccam-restart','Restart CCCam',this)"><i class="fas fa-sync-alt"></i> Restart CCCam</div>
            </div>
            <div class="menu-item" onclick="toggleSub(this)">
                <i class="fas fa-satellite-dish"></i> MGcamd <i class="fas fa-chevron-right submenu-arrow"></i>
            </div>
            <div class="submenu">
                <div class="menu-item" onclick="navigateTo('mgcamd-add','Adicionar Servidor MGcamd',this)"><i class="fas fa-plus-circle"></i> Adicionar Servidor</div>
                <div class="menu-item" onclick="navigateTo('mgcamd-list','Listar Servidores MGcamd',this)"><i class="fas fa-list"></i> Listar Servidores</div>
                <div class="menu-item" onclick="navigateTo('mgcamd-lines','Gerar MG-Lines',this)"><i class="fas fa-key"></i> Gerar MG-Lines</div>
            </div>
            <div class="menu-item" onclick="toggleSub(this)">
                <i class="fas fa-broadcast-tower"></i> Newcamd <i class="fas fa-chevron-right submenu-arrow"></i>
            </div>
            <div class="submenu">
                <div class="menu-item" onclick="navigateTo('newcamd-add','Adicionar Servidor Newcamd',this)"><i class="fas fa-plus-circle"></i> Adicionar Servidor</div>
                <div class="menu-item" onclick="navigateTo('newcamd-list','Listar Servidores Newcamd',this)"><i class="fas fa-list"></i> Listar Servidores</div>
                <div class="menu-item" onclick="navigateTo('newcamd-lines','Gerar N-LINES',this)"><i class="fas fa-key"></i> Gerar N-Lines</div>
            </div>
            <div class="menu-item" onclick="navigateTo('oscam','Servidor OSCam',this)"><i class="fas fa-microchip"></i> OSCam</div>
            <div class="menu-item" onclick="navigateTo('csp','Servidor CSP',this)"><i class="fas fa-network-wired"></i> CSP</div>

            <div class="menu-header">Gerenciar</div>
            <div class="menu-item" onclick="navigateTo('admin','Administrador',this)"><i class="fas fa-shield-alt"></i> Administrador</div>
            <div class="menu-item" onclick="navigateTo('revendedor','Revendedor',this)"><i class="fas fa-store"></i> Revendedor</div>
            <div class="menu-item" onclick="navigateTo('usuarios-cs','Usuários CS',this)"><i class="fas fa-users"></i> Usuários CS</div>
            <div class="menu-item" onclick="navigateTo('testes','Testes CS',this)"><i class="fas fa-vial"></i> Testes</div>
            <div class="menu-item" onclick="navigateTo('online','Conexões Online',this)"><i class="fas fa-wifi"></i> Online</div>

            <div class="menu-header">Linhas / Clines</div>
            <div class="menu-item" onclick="navigateTo('gerar-clines','Gerar C-Lines',this)"><i class="fas fa-key"></i> Gerar C-Lines</div>
            <div class="menu-item" onclick="navigateTo('minhas-linhas','Minhas Linhas',this)"><i class="fas fa-file-alt"></i> Minhas Linhas</div>
            <div class="menu-item" onclick="navigateTo('linhas-expiradas','Linhas Expiradas',this)"><i class="fas fa-clock"></i> Linhas Expiradas</div>
            <div class="menu-item" onclick="navigateTo('linhas-bloqueadas','Linhas Bloqueadas',this)"><i class="fas fa-ban"></i> Linhas Bloqueadas</div>

            <div class="menu-header">Pagamentos</div>
            <div class="menu-item" onclick="navigateTo('comprar-creditos','Comprar Créditos',this)"><i class="fas fa-shopping-cart"></i> Comprar Créditos</div>
            <div class="menu-item" onclick="navigateTo('minhas-compras','Minhas Compras',this)"><i class="fas fa-receipt"></i> Minhas Compras</div>
            <div class="menu-item" onclick="navigateTo('minhas-vendas','Minhas Vendas',this)"><i class="fas fa-exchange-alt"></i> Minhas Vendas</div>
            <div class="menu-item" onclick="navigateTo('criar-plano','Criar Plano CS',this)"><i class="fas fa-credit-card"></i> Criar Plano CS</div>
            <div class="menu-item" onclick="navigateTo('pagseguro','PagSeguro',this)"><i class="fab fa-pagseguro"></i> PagSeguro</div>
            <div class="menu-item" onclick="navigateTo('paypal','PayPal',this)"><i class="fab fa-paypal"></i> PayPal</div>
            <div class="menu-item" onclick="navigateTo('mercadopago','MercadoPago',this)"><i class="fas fa-money-check-alt"></i> MercadoPago</div>

            <div class="menu-header">Redes Sociais</div>
            <div class="menu-item" onclick="navigateTo('whatsapp','WhatsApp',this)"><i class="fab fa-whatsapp"></i> WhatsApp</div>
            <div class="menu-item" onclick="navigateTo('telegram','Telegram',this)"><i class="fab fa-telegram"></i> Telegram</div>

            <div class="menu-header">Relatório</div>
            <div class="menu-item" onclick="navigateTo('relatorios','Relatórios',this)"><i class="fas fa-chart-bar"></i> Relatórios</div>
            <div class="menu-item" onclick="navigateTo('estatisticas','Estatísticas',this)"><i class="fas fa-chart-line"></i> Estatísticas</div>

            <div class="menu-header">Configurações</div>
            <div class="menu-item" onclick="navigateTo('config-servidor','Config. Servidor',this)"><i class="fas fa-cogs"></i> Config. Servidor</div>
            <div class="menu-item" onclick="navigateTo('email','Email',this)"><i class="fas fa-envelope"></i> Email</div>
            <div class="menu-item" onclick="navigateTo('sms','SMS',this)"><i class="fas fa-sms"></i> SMS</div>
            <div class="menu-item" onclick="navigateTo('seguranca','Segurança',this)"><i class="fas fa-shield-alt"></i> Segurança</div>

            <div class="menu-header">Opções</div>
            <div class="menu-item" onclick="navigateTo('opcoes','Opções',this)"><i class="fas fa-sliders-h"></i> Opções</div>

            <div class="menu-header">Suporte</div>
            <div class="menu-item" onclick="navigateTo('suporte','Suporte',this)"><i class="fas fa-headset"></i> Suporte</div>

            <div class="menu-header">Template</div>
            <div class="menu-item" onclick="navigateTo('template','Template',this)"><i class="fas fa-palette"></i> Template</div>

            <div class="sidebar-pro-badge">
                <img src="data:image/png;base64,{ico_b64}" alt="CS" style="border-radius:8px">
                <div>HomerFull CS PRO</div>
                <div style="font-size:9px;opacity:.8">Card Sharing Manager</div>
            </div>
            <div class="sidebar-version">HomerFull CS Panel v3.0<br>&copy; 2026</div>
        </div>
    </div>

    <!-- Top Bar -->
    <div class="topbar">
        <div class="topbar-left">
            <i class="fas fa-bars" onclick="toggleSidebar()"></i>
            <span class="topbar-page-title" id="topbar-title">Início</span>
        </div>
        <div class="topbar-right">
            <div class="notif"><i class="fas fa-bell"></i><span class="badge">3</span></div>
            <i class="fas fa-expand" onclick="document.documentElement.requestFullscreen?.()" style="cursor:pointer"></i>
            <div class="user-info">
                <div class="user-avatar">A</div>
                <span>Admin</span>
                <i class="fas fa-chevron-down" style="font-size:10px"></i>
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        {all_sections}
    </div>
</div>

<script>
function showView(view) {{
    const lv = document.getElementById('login-view');
    const dv = document.getElementById('dashboard-view');
    const btns = document.querySelectorAll('.view-toggle button');
    btns.forEach(b => b.classList.remove('active'));
    if (view === 'login') {{
        lv.style.display = 'flex'; dv.style.display = 'none'; btns[0].classList.add('active');
    }} else {{
        lv.style.display = 'none'; dv.style.display = 'block'; btns[1].classList.add('active');
        // Show home by default
        navigateTo('inicio', 'Início');
    }}
}}

function navigateTo(sectionId, title, clickedItem) {{
    // Hide all sections
    document.querySelectorAll('.section-page').forEach(el => el.style.display = 'none');
    // Show target section
    const target = document.getElementById('sec-' + sectionId);
    if (target) {{
        target.style.display = 'block';
    }}
    // Update topbar title
    const tt = document.getElementById('topbar-title');
    if (tt && title) tt.textContent = title;
    // Update active sidebar item
    if (clickedItem) {{
        document.querySelectorAll('.sidebar-menu .menu-item').forEach(el => el.classList.remove('active'));
        clickedItem.classList.add('active');
    }}
}}

function toggleSidebar() {{
    const sb = document.querySelector('.sidebar');
    const tb = document.querySelector('.topbar');
    const mc = document.querySelector('.main-content');
    if (sb.style.width === '0px') {{
        sb.style.width = '250px'; sb.style.transform = 'translateX(0)';
        tb.style.left = '250px'; mc.style.marginLeft = '250px';
    }} else {{
        sb.style.width = '0px'; sb.style.transform = 'translateX(-100%)';
        tb.style.left = '0'; mc.style.marginLeft = '0';
    }}
}}

function toggleSub(el) {{
    const sub = el.nextElementSibling;
    if (sub && sub.classList.contains('submenu')) {{
        sub.classList.toggle('show'); el.classList.toggle('open');
    }}
}}

function copyLine(btn) {{
    const value = btn.parentElement.querySelector('.cline-value').textContent;
    navigator.clipboard?.writeText(value).then(() => {{
        const orig = btn.textContent;
        btn.textContent = '✓ Copiado!';
        btn.style.background = '#28a745';
        setTimeout(() => {{ btn.textContent = orig; btn.style.background = '#6967CE'; }}, 1500);
    }}).catch(() => {{
        alert('Linha: ' + value);
    }});
}}

// Start on dashboard home
navigateTo('inicio', 'Início');
</script>
</body>
</html>'''

with open('/nfs/103214813/outputs/painel-cs-preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"CS Panel mockup written: {len(html):,} bytes")
print(f"Sections: {len(sections)}")
