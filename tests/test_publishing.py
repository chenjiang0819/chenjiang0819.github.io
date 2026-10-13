"""Local Chrome regressions; external resources and submissions are blocked."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import os,threading,unittest
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
class BrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tmp=ROOT/'.build/browser-temp';tmp.mkdir(parents=True,exist_ok=True);os.environ['TMPDIR']=str(tmp)
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT)))
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.url=f'http://127.0.0.1:{cls.server.server_port}/'
        cls.pw=sync_playwright().start()
        cls.browser=cls.pw.chromium.launch(channel='chrome',headless=True)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.pw.stop();cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def context(self,width,height):
        context=self.browser.new_context(viewport={'width':width,'height':height})
        context.route('**/*',lambda route:route.continue_() if route.request.url.startswith(self.url) else route.abort())
        self.addCleanup(context.close);return context
    def test_root_entry(self):
        context=self.context(1280,900);page=context.new_page()
        page.goto(self.url,wait_until='networkidle')
        self.assertTrue(page.url.endswith('/home.html'));self.assertEqual(page.locator('img').evaluate_all('(xs)=>xs.filter(x=>!x.naturalWidth).length'),0)
    def test_original_pages_and_assets(self):
        context=self.context(1280,900)
        for file in sorted(ROOT.glob('*.html')):
            with self.subTest(file=file.name):
                page=context.new_page();errors=[];failed=[]
                page.on('pageerror',lambda error:errors.append(str(error)))
                page.on('response',lambda r:failed.append(r.url) if r.status>=400 else None)
                page.goto(self.url+file.name,wait_until='networkidle')
                self.assertFalse(errors);self.assertFalse(failed);self.assertEqual(page.evaluate('Array.from(document.images).filter(x=>!x.complete||!x.naturalWidth).length'),0)
                page.close()
if __name__=='__main__':unittest.main()
