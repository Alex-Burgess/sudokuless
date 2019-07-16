window._config = {
    cognito: {
        userPoolId: 'eu-west-1_2eF2vZyKX', // e.g. us-east-2_uXboG5pAb
        userPoolClientId: 'rp869po59eb66kflg5p25jgj7', // e.g. 25ddkmj4v6hfsfvruhpfi7n4hv
        appWebDomain: 'sudokuless-staging.auth.eu-west-1.amazoncognito.com', // Exclude the "https://" part.
        redirectUriSignIn: 'https://staging.sudokuless.com/signin/',
        redirectUriSignOut: 'https://staging.sudokuless.com/',
        identityProvider: 'LoginWithAmazon',
        region: 'eu-west-1' // e.g. us-east-2
    },
    api: {
        requestNewPuzzleUrl: 'https://ej4xecnx14.execute-api.eu-west-1.amazonaws.com/staging/tryNewPuzzle/',
        getNewPuzzleSolutionUrl: 'https://pdkvj7254c.execute-api.eu-west-1.amazonaws.com/staging/getNewPuzzleSolution/',
        solvePuzzle: 'https://nrvt0b0zoc.execute-api.eu-west-1.amazonaws.com/staging/solvePuzzle/'
    }
};
