# Lumina Contabilidade — Teste Técnico Mupi Systems 🚀

Aplicação web full stack desenvolvida para o processo seletivo da Mupi Systems.
Plataforma para um escritório de contabilidade fictício ("Lumina"), com:

- Página pública (Landing Page) para captação de clientes
- Página de login para o administrador acessar o painel.
- Painel administrativo para gestão de mensagens de contato
---

## Funcionalidades

### Área pública (Landing Page)

- Design responsivo usando TailwindCSS
- Seções informativas: serviços, preços, depoimentos e parceiros
- Formulário de contato com validação via Django Forms
- Sanitização do telefone (salva somente dígitos)
- Feedback visual (mensagens de sucesso/erro)

### Área administrativa (Painel)

- Acesso restrito a administradores (superusuários)
- Dashboard com estatísticas: Total, Lidas, Não lidas
- Listagem de mensagens com filtros (Todas / Lidas / Não lidas)
- Ações: marcar como lida/não lida, excluir (POST + confirmação)

---

## Tecnologias

### Stack Principal

- **Backend:** Python 3.10+, Django 6.0
- **Frontend:** HTML5, TailwindCSS (CDN), Lucide Icons
- **Banco de dados:** SQLite3 (padrão)

### Ferramentas de Desenvolvimento

- **Gerenciador de Pacotes:** uv (para instalações rápidas e gerenciamento de dependências)

- **Linting e Formatação:** Ruff (configurado via pyproject.toml para garantir qualidade de código)

---

## Estrutura do projeto (resumida)

```
.
├── contabilidade/
│   ├── templates/
│   │   ├── partials/    # componentes reutilizáveis (header, footer, cards)
│   │   ├── base.html
│   │   ├── landpage.html
│   │   ├── login.html
│   │   └── panel.html
│   ├── forms.py         # validação e sanitização de formulários
│   ├── models.py        # modelo Message
│   ├── views.py         # lógica e controle de acesso
│   └── urls.py          # rotas do app
├── core/                # configurações do projeto
├── manage.py
└── requirements.txt
```

---

## Instalação e execução (ambiente local)

Pré-requisitos: Python 3.10+ e Git

1. Clone o repositório

```bash
git clone https://github.com/YagoMaia/projeto_estagio_2026_1
cd projeto_estagio_2026_1
```

2. Crie e ative um ambiente virtual

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale dependências

```bash
pip install -r requirements.txt
```

4. Aplique migrações

```bash
py manage.py migrate
```

5. (Opcional) Crie um superusuário

```bash
py manage.py createsuperuser
```

6. Execute o servidor de desenvolvimento

```bash
py manage.py runserver
```

Acessos úteis:

- Site: http://127.0.0.1:8000/
- Login admin: http://127.0.0.1:8000/login/
- Painel: http://127.0.0.1:8000/painel/

---

## Diferenciais implementados

Além dos requisitos básicos, foram adicionadas as seguintes melhorias para enriquecer a experiência do usuário e a qualidade do código:

- [x] **Tratamento de Dados:** Sanitização automática do campo telefone no backend (``clean_phone``).
- [x] **UX Aprimorada:** Feedback visual com mensagens de sucesso/erro estilizadas e responsivas.
- [x] **Filtros e Estatísticas:** Dashboard administrativo com contadores e filtros de estado de leitura.
- [x] **Segurança:** Proteção CSRF em todos os formulários e ações de exclusão/edição via método POST.
- [x] **Organização:** Uso extensivo de Template Partials para manter o código HTML limpo e modular.

## Autor

Desenvolvido por **Yago Henrique Veloso Maia** para o processo seletivo da Mupi Systems.
