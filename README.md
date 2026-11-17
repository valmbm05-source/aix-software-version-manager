# aix-software-version-manager
A Python-based application for managing software inventory, installed versions, and upgrade planning across IBM AIX servers.
## Development Roadmap. 
### Phase 1 – Development Environment Setup
- [x] Create GitHub repository
- [x] Create initial Python application (`app.py`)
- [ ] Install and configure Python
- [ ] Configure local development environment

### Phase 2 – Software Inventory Import
- [ ] Implement Excel (.xlsx) file import
- [ ] Implement CSV file import
- [ ] Support multiple software installations per AIX server
- [ ] Validate imported inventory data

### Phase 3 – Database Implementation
- [ ] Design SQLite database structure
- [ ] Create server and software tables
- [ ] Store installed software versions
- [ ] Prevent duplicate inventory records
- [ ] Track inventory import history

### Phase 4 – Software Version Management
- [ ] Track installed and approved software versions
- [ ] Identify software requiring upgrades
- [ ] Manage upgrade status and priorities
- [ ] Maintain software upgrade history

### Phase 5 – Web Interface and Dashboard
- [ ] Develop web interface using Streamlit
- [ ] Implement inventory file upload
- [ ] Create server and software search functionality
- [ ] Develop compliance and upgrade dashboards
- [ ] Generate inventory and upgrade reports

### Phase 6 – Testing and Quality Assurance
- [ ] Implement automated tests
- [ ] Validate inventory processing and database operations
- [ ] Handle errors and invalid input files
- [ ] Document technical decisions and test results

### Phase 7 – Future Enhancements
- [ ] Support AIX command output files (`oslevel`, `lslpp`, `rpm`)
- [ ] Implement secure automated inventory collection
- [ ] Add multi-client support and user access controls
- [ ] Improve scalability and deployment options
  
