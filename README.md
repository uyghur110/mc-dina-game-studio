# MC DINA GAME STUDIO website

A separate, dependency-free HTML/CSS/JavaScript project. No Unity or Godot files were accessed or changed. Nothing has been published.

## Preview locally
Open index.html in a browser. No installation or build is needed. To check phone and tablet layouts, use your browser developer tools at 390, 768 and 1440 px, and test on a real phone before release.

## Free GitHub Pages deployment — only after you approve
1. Create a free GitHub account if needed, then create a public repository named mc-dina-game-studio. Public means your website source will be visible. Do not upload your Unity project or private information.
2. Decide the final URL: https://USERNAME.github.io/mc-dina-game-studio/ (replace USERNAME).
3. If Python is already installed, run `python configure.py https://USERNAME.github.io/mc-dina-game-studio/` in this folder. Alternatively manually add canonical and og:url tags to index.html, the real URL to sitemap.xml, and its address to robots.txt. The final URL is now configured as https://uyghur110.github.io/mc-dina-game-studio/. The sitemap, robots.txt, canonical tag and og:url use that approved address. No further URL setup is needed unless the address changes.
4. Upload the contents of this folder to the repository root, including .nojekyll. Do not upload the outer folder or ZIP itself. No package install or build is required.
5. Once you are ready to publish, open repository Settings → Pages → Build and deployment → Deploy from a branch. Select main and / (root), then Save. This step publishes the website. No paid domain is needed.
6. Wait for GitHub's Pages deployment to finish and open the URL shown in Settings → Pages. Confirm navigation, gallery labels, contact placeholder, and YouTube links on desktop and phone.

## Editing
- Copy and sections: index.html.
- Palette, spacing, breakpoints: styles.css.
- Mobile menu: script.js. Navigation also works without JavaScript.
- Decorative background: assets/forest.svg, original vector website artwork, NOT a gameplay screenshot.
- There is no provided studio logo, so the header uses a plain text studio name.
- Gallery: replace each placeholder-content div with an img using an actual supplied Unity screenshot. Give it descriptive alt text; use width/height, loading="lazy", width:100%;height:auto. Remove the placeholder wording only once real screenshots are present.
- Contact: replace the placeholder with an approved public email and mailto link. There is intentionally no inactive form or fake email.
- Development: add only verified updates; no completion percentages or release dates are invented.
- Social previews: Open Graph text is included. No og:image is included because no approved studio/game image was supplied; add a real 1200×630 image and its absolute URL when approved. SVG support across social platforms is inconsistent.

## Privacy and assets
No analytics, cookies, external fonts, video embeds, trackers, third-party logos or external image dependencies. YouTube opens only when a visitor follows a link. The subscribe link leads to YouTube; it does not subscribe automatically.

## Verification limits
Source and link checks can be run without a browser. Actual mobile and desktop rendering still requires browser review. Do not interpret responsive CSS as a completed visual-device test.
