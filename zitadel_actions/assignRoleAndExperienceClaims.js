function assignRoleAndExperienceClaims(ctx, api) {
    // Check if grants and metadata exist
    if (!ctx.v1.user.grants || !ctx.v1.claims['urn:zitadel:iam:user:metadata']) {
        return;
    }

    // Decode experience level from Base64 - metadata is Base64 encoded
    let experience_encoded = ctx.v1.claims['urn:zitadel:iam:user:metadata'].experience_level;
    let experience = '';
    try {
        experience = decodeURIComponent(escape(String.fromCharCode.apply(null, experience_encoded.split('').map(function(c) {
            return '0x' + ('0' + c.charCodeAt(0).toString(16)).slice(-2);
        }))));
    } catch (e) {
        return; // If decoding fails, stop executing the function
    }

    // Check if the experience level exists
    if (!experience) {
        return;
    }

    // Iterate through the user's grants
    ctx.v1.user.grants.grants.forEach(grant => {
        // Iterate through the roles of each grant
        grant.roles.forEach(role => {
            // Check if the user is a journalist
            if (role === 'journalist') {
                // Set custom claims with the user's role and experience level
                api.v1.claims.setClaim('journalist:experience_level', experience);
            }
            // Check if the user is an editor
            else if (role === 'editor') {
                // Set custom claims with the user's role and experience level
                api.v1.claims.setClaim('editor:experience_level', experience);
            }
        });
    });
}
