const HOST = "htpp://127.0.0.1:8000";
const VERSION = "V1";


// update this with project api endpoints from django
export default {
    CAMPAIGNS: [HOST, VERSION, "campaings"].join("/")
};